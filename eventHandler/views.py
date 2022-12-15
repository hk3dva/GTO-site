from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views.generic import DetailView, DeleteView, UpdateView
from django.contrib.auth.models import Group, User

# Create your views here.
def index(request):
    eventNameList = Event.objects.all()
    teamList = Team.objects.all()
    userList = AuthUser.objects.all()
    trainerList = User.objects.filter(groups__name='trainers')
    sportsmansList = User.objects.filter(groups__name='sportsman')

    sportList = SportType.objects.all()
    SportObjectList = SportObject.objects.all()
    context = {
        'events' : eventNameList,
        'teams' : teamList,
        'users' : userList,
        'trainers' : trainerList,
        'sportsmans' : sportsmansList,
        'sports' : sportList,
        'objects' : SportObjectList,
    }
    return render(request, 'eventHandler/event.html', context)

def sportCreate(request):
    if request.method == "POST":
        form = createSportType(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/event')
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
            return redirect('/event')
    else:
        form = createSportObject()

    context = {
        'form' : form,
    }
    return render(request, 'eventHandler/sportObjectCreate.html', context)

def SportTypeEventcreate(request):
    if request.method == "POST":
        form = createSportTypeEvent(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/event')
    else:
        form = createSportTypeEvent()

    context = {
        'form': form,
    }
    return render(request, 'eventHandler/SportTypeEventcreate.html', context)

def createEvent(request):
    if request.method == "POST":
        form = createEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/event')
    else:
        form = createEventForm()

    # form.fields["persons"].queryset = User.objects.filter(groups__name='sportsman')

    context = {
        'form' : form,
    }
    return render(request, 'eventHandler/eventCreate.html', context)

def trainerAppoin(request):
    if request.method == "POST":
        form = appoinTrainerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("names")
            for el in name:
                el.groups.clear()
                Group.objects.get(name='trainers').user_set.add(el)
        return redirect('/event')
    else:
        form = appoinTrainerForm()

    context = {
        'form' : form,
    }
    return render(request, 'eventHandler/appointTrainer.html', context)

class eventUpdate(UpdateView):
    model = Event
    template_name = 'eventHandler/eventUpdate.html'
    form_class = createEventForm

class eventDelete(DeleteView):
    model = Event
    success_url = '/event'
    template_name = 'eventHandler/eventDelete.html'


def teamCreate(request):
    if request.method == "POST":
        form = createTeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/event')
    else:
        form = createTeamForm()

    context = {
        'form' : form,
    }
    return render(request, 'eventHandler/team.html', context)

class teamUpdate(UpdateView):
    model = Team
    template_name = 'eventHandler/teamUpdate.html'
    form_class = createTeamForm

class teamDelete(DeleteView):
    model = Team
    success_url = '/event'
    template_name = 'eventHandler/teamDelete.html'