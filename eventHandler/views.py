from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views.generic import DetailView, DeleteView, UpdateView


# Create your views here.
def index(request):
    eventNameList = Event.objects.all()
    teamList = Team.objects.all()
    context = {
        'mp' : eventNameList,
        'team' : teamList,
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

def compoundCreate(request):
    if request.method == "POST":
        form = createCompound(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/event')
    else:
        form = createCompound()

    context = {
        'form' : form,
    }
    return render(request, 'eventHandler/compound.html', context)

def createEvent(request):
    if request.method == "POST":
        form = createEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/event')
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