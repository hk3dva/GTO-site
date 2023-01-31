from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import Group


def register(request):
    if request.method == "POST":
        registerForm = customCreateUser(request.POST)
        if registerForm.is_valid():
            t = registerForm.save()
            Group.objects.get(name='sportsman').user_set.add(t)

            return redirect('/')
    else:
        registerForm = customCreateUser()

    context = {
        'title' : 'Страница Регистрации',
        'form' : registerForm,
    }
    return render(request, 'registrationUser/register.html', context)


def logOut(request):
    logout(request)
    return redirect('/')

def index(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == "POST":
        loginForm = AuthenticationForm(request=request,data=request.POST)
        if loginForm.is_valid():
            uname = loginForm.cleaned_data['username']
            upass = loginForm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request,user)
                return redirect('/')
    else:
        loginForm = AuthenticationForm()

    context = {
        'form' : loginForm,
    }
    return render(request, 'registrationUser/index.html', context)

