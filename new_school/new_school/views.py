from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def change(request):
    user_text = request.GET['usertext']
    return render(request, 'change.html',
                  context={'usertext': user_text})

def confirm(request):
    return render(request, 'confirm.html')