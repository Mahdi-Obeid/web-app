from django.shortcuts import render

# Create your views here.

def createApp(request):
    posts = 'hello'

    return render(request, 'main.html',{'posts':posts})