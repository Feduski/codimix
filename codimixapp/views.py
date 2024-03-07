from django.shortcuts import render, HttpResponse
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os 

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

def home(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        return render(request, 'base.html', {'user_sent' : user_input})

    return render(request, 'base.html')

"""    if request.method == 'POST':
        user_input = request.POST.get('user_input')

        prompt_template = os.getenv("TEMPLATE")
        
        message = llm.invoke(prompt_template, query = user_input)

        return render(request, 'base.html', {'user_sent': message.content})"""