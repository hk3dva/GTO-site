from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views.generic import DetailView, DeleteView, UpdateView


# Create your views here.
def getBaseContext():
    eventNameList = Event.objects.all()
    teamList = Team.objects.all()
    organizationList = Organization.objects.all()
    userList = AuthUser.objects.all()
    compounds = Compound.objects.all()
    sportTypes = TypeSport.objects.all()
    context = {
        'mp': eventNameList,
        'team': teamList,
        'org': organizationList,
        'users': userList,
        'compound': compounds,
        'sportTypes': sportTypes
    }
    return context

def index(request):
    return render(request, 'eventHandler/index.html', getBaseContext())

def sportCreate(request):
    if request.method == "POST":
        form = createSportType(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sportType')
    else:
        form = createSportType()

    context = {
        'form' : form,
    }
    return render(request, 'eventHandler/sportCreate.html', context)

def sportObjectCreate(request):
    if request.method == "POST":
        form = createSportObject(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/organization')
    else:
        form = createSportObject()

    context = {
        'form' : form,
    }
    return render(request, 'eventHandler/sportObjectCreate.html', context)

def sportType(request):
    return render(request, 'eventHandler/sportType.html', getBaseContext())

def users(request):
    return render(request, 'eventHandler/users.html', getBaseContext())

class userUpdate(UpdateView):
    model = AuthUser
    template_name = 'eventHandler/userUpdate.html'
    form_class = createUser

# def userUpdate(request):
#     if request.method == "POST":
#         form = createUser(request.POST)
#         if form.is_valid():
#             form.password = make_password(form.password)
#             form.save()
#             return redirect('/event')
#     else:
#         form = createUser()
#
#     context = {
#         'form' : form,
#     }
#     return render(request, 'eventHandler/UserResultCreate.html', context)

class userDelete(DeleteView):
    model = AuthUser
    success_url = '/users'
    template_name = 'eventHandler/userDelete.html'

def UserResultCreate(request):
    if request.method == "POST":
        form = createUserResult(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users')
    else:
        form = createUserResult()

    context = {
        'form' : form,
    }
    return render(request, 'eventHandler/UserResultCreate.html', context)

class UserResultUpdate(UpdateView):
    model = UserResult
    template_name = 'eventHandler/UserResultCreate.html'
    form_class = createUserResult

def compound(request):
    return render(request, 'eventHandler/groups.html', getBaseContext())

def compoundCreate(request):
    if request.method == "POST":
        form = createCompound(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/groups')
    else:
        form = createCompound()

    context = {
        'form' : form,
    }
    return render(request, 'eventHandler/compound.html', context)

def organization(request):
    return render(request, 'eventHandler/organization.html', getBaseContext())

def organizationСreate(request):
    if request.method == "POST":
        form = createOrganization(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/organization')
    else:
        form = createOrganization()

    context = {
        'form' : form,
    }
    return render(request, 'eventHandler/organizationCreate.html', context)

def events(request):
    return render(request, 'eventHandler/events.html', getBaseContext())

def createEvent(request):
    if request.method == "POST":
        form = createEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/events')
    else:
        form = createEventForm()

    context = {
        'form' : form,
    }
    return render(request, 'eventHandler/eventCreate.html', context)

class eventUpdate(UpdateView):
    model = Event
    template_name = 'eventHandler/eventUpdate.html'
    form_class = createEventForm

class eventDelete(DeleteView):
    model = Event
    success_url = '/events'
    template_name = 'eventHandler/eventDelete.html'

def team(request):
    return render(request, 'eventHandler/team.html', getBaseContext())

def teamCreate(request):
    if request.method == "POST":
        form = createTeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/team')
    else:
        form = createTeamForm()

    context = {
        'form' : form,
    }
    return render(request, 'eventHandler/teamCreate.html', context)

class teamUpdate(UpdateView):
    model = Team
    template_name = 'eventHandler/teamUpdate.html'
    form_class = createTeamForm

class teamDelete(DeleteView):
    model = Team
    success_url = '/teams'
    template_name = 'eventHandler/teamDelete.html'