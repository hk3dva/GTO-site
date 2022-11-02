from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .forms import createEventForm


# Create your views here.
def register(request):
    if request.method == "POST":
        registerForm = UserCreationForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()
            return redirect('/resReg')
    else:
        registerForm = UserCreationForm()

    context = {
        'title' : 'Страница Регистрации',
        'form' : registerForm,
    }
    return render(request, 'registrationUser/register.html', context)

def resReg(request):
    return render(request, 'registrationUser/resReg.html')

def resLog(request):
    return render(request, 'registrationUser/resLog.html')

def Log(request):
    return render(request, 'registrationUser/Log.html')

def logIn(request):
    if request.user.is_authenticated:
        return render(request, 'registrationUser/Log.html')

    if request.method == "POST":
        loginForm = AuthenticationForm(request=request,data=request.POST)
        if loginForm.is_valid():
            uname = loginForm.cleaned_data['username']
            upass = loginForm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request,user)
                return render(request, 'registrationUser/resLog.html')
    else:
        loginForm = AuthenticationForm()
    return render(request,'registrationUser/login.html', {'form':loginForm})



def logOut(request):
    logout(request)
    return redirect('/')

def index(request):

    username = 'Аноним'
    if request.user.is_authenticated:
        username = request.user.username
    context = {
        'name': username
    }
    return render(request, 'registrationUser/index.html', context)


def createEvent(request):
    if request.method == "POST":
        form = createEventForm(request.POST)
        if form.is_valid():
            return render(request, 'registrationUser/resCreate.html',
                          {
                              'name' : form.cleaned_data['name'],
                              'members' : form.cleaned_data['members']
                          })
    else:
        form = createEventForm()

    context = {
        'form' : form,
    }
    return render(request, 'registrationUser/Event.html', context)

def resCreate(request):
    name = ''
    context = {
        'name' : name,
    }
    return render(request, 'registrationUser/resCreate.html', context)