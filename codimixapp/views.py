from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from dotenv import load_dotenv, dotenv_values
from django.db import IntegrityError
from django.http import JsonResponse
from openai import OpenAI
import os 

load_dotenv()
OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")
env_vars = dotenv_values("codimixapp\.env")
prompt_template = env_vars.get("TEMPLATE")
client = OpenAI(api_key=OPEN_AI_KEY)

def home(request):
    return render(request, 'home.html')

def base(request):
    return render(request, 'base.html')

@login_required(login_url='login.html')
def process_user_input(request):
    if not request.user.is_authenticated:
        print('User not authenticated')
        """return render(request, 'home.html', {
            'error_message': 'Error: You must be logged in to use this feature.'
        })"""
    elif request.user.credits < 1:
        print('No more credits')
        """return render(request, 'home.html', {
            'error_message': 'Error: Not enough credits.'
        })"""

    else:
        request.user.credits -= 1
        request.user.save()
        user_input = request.GET.get('user_input')
        selected_language = request.GET.get('selected_language')
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt_template.format(language = selected_language)},
                {"role": "user", "content": user_input},
            ]
        )
        user_sent_to = completion.choices[0].message.content
        return JsonResponse({'user_sent' : user_sent_to, 'selected_language': selected_language})

def register_view(request):
    if request.method == 'GET':
        return render(request, 'register.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] != request.POST['password2']:
            print('Passwords do not match')
            return render(request, 'register.html', {
                'form': UserCreationForm,
                'error': 'Passwords do not match'
            })

        else:
            try:
                print('Creating user')
                user = CustomUser.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'],
                )
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError as e:
                print(f'User already exists, {e}')
                return render(request, 'register.html', {
                    'form': UserCreationForm,
                    'error': 'User already exists'
                })
            except Exception as e:
                print(f'Error creating user, {e}')
                return render(request, 'register.html', {
                    'form': UserCreationForm,
                    'error': 'Error creating user'
                })

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html', {'form': AuthenticationForm()})
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {
                'form': AuthenticationForm(),
                'error': 'Invalid username or password'
            })
        
def testing_files(request):
    users = CustomUser.objects.all()
    return render(request, 'testing.html', {'users': users})