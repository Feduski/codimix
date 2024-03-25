from django.shortcuts import render, HttpResponse, redirect
from dotenv import load_dotenv
from django.http import JsonResponse
import os 

load_dotenv()
OPEN_AI_KEY = os.getenv("OPEN_AI_KEY")


def home(request):
    return render(request, 'base.html')

def process_user_input(request):
    user_input = request.GET.get('user_input')
    selected_language = request.GET.get('selected_language')
    return JsonResponse({'user_sent' : user_input, 'selected_language': selected_language})