from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, User

def index(request):
    username = 'Аноним'
    if request.user.is_authenticated:
        username = request.user.username

    context = {
        'title' : 'Сайт для автоматизации ГТО',
        'name' : username
    }
    return render(request, 'index.html', context)

def info(request):
    context = {
        'title' : 'Информация о ГТО',
    }
    return render(request, 'base.html', context)

def smi(request):
    context = {
        'title' : 'Сайт для автоматизации ГТО',
    }
    return render(request, 'index.html', context)

def partners(request):
    context = {
        'title' : 'Сайт для автоматизации ГТО',
    }
    return render(request, 'index.html', context)

