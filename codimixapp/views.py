from django.shortcuts import render, HttpResponse
from langchain_google_genai import ChatGoogleGenerativeAI
import os 

# Create your views here.

def home(request):
    if request.method == 'POST':
        #user_question = request.POST.get('user_input', '')
        
        #llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=os.environ.get("GOOGLE_API_KEY"))
        #try:   
        #    message = llm.invoke(user_question)
        #except:
        #    pass
        return render(request, 'base.html') #{'user_response': message.content }

    return render(request, 'base.html')