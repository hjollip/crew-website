
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def home(request):
    return render(request,'home.html')

def login_view(request):
    error=None
    if request.method=='POST':
        user=authenticate(request,
            username=request.POST.get('username'),
            password=request.POST.get('password'))
        if user:
            login(request,user)
            return redirect('chatbot')
        error='Invalid credentials'
    return render(request,'login.html',{'error':error})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def chatbot(request):
    history=request.session.get('history',[])
    if request.method=='POST':
        msg=request.POST.get('message')
        history.append({'role':'user','content':msg})
        history=history[-20:]
        resp=client.chat.completions.create(
            model='gpt-4o-mini',
            messages=history
        )
        ans=resp.choices[0].message.content
        history.append({'role':'assistant','content':ans})
        history=history[-20:]
        request.session['history']=history
    return render(request,'chatbot.html',{'history':history})
