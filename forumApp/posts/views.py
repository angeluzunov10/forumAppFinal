from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):

    context = {
        "current_time": datetime.now(),
        "some_text": "Hello my name is Angel and I am a developer!"
    }

    return render(request, 'base.html', context=context)


def dashboard(request):
    context = {
        "posts":[
            {
                "title": "How to create Django project?",
                "author": "Angel Uzunov",
                "content": "I **really** want to know how to create Django project.",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create Django project 1?",
                "author": "",
                "content": "I really want to know how to create Django project.",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create Django project 2?",
                "author": "Angel Uzunov",
                "content": "",
                "created_at": datetime.now(),
            },

        ]
    }

    return render(request, 'posts/dashboard.html', context=context)