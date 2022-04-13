import imp
from inspect import ismethoddescriptor
from django.shortcuts import render
from .models import Post, Messages
def home(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'details/about.html')

def chat(request):
    posts = Post.objects.all()
    messages = Messages.objects.all()
    context = {
        'posts':posts,
        'messages':messages
    }
    
    return render(request, 'chat.html', context)