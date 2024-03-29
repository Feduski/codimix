from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from dotenv import load_dotenv, dotenv_values
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

def process_user_input(request):
    user_input = request.GET.get('user_input')
    print(user_input)
    selected_language = request.GET.get('selected_language')
    print(selected_language)
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
                'form': UserCreationForm(),
                'error': 'Passwords do not match'
            })

        else:
            try:
                print('Creating user')
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1']
                )
                user.save()
                return render(request, 'register.html', {
                'form': UserCreationForm(),
                'error': 'USER CREATED'
                })
            except:
                print('User already exists')
                return render(request, 'register.html', {
                    'form': UserCreationForm(),
                    'error': 'User already exists'
                })