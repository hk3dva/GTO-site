from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views.generic import DetailView, DeleteView, UpdateView


# Create your views here.
def index(request):
    eventNameList = Event.objects.all()
    teamList = Team.objects.all()
    organizationList = Organization.objects.all()
    userList = AuthUser.objects.all()
    context = {
        'mp' : eventNameList,
        'team' : teamList,
        'org' : organizationList,
        'user' : userList,
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

def UserResultCreate(request):
    if request.method == "POST":
        form = createUserResult(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/event')
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

def compoundCreate(request):
    if request.method == "POST":
        form = createCompound(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/event')
    else:
        form = createCompound()

    form.fields["trainers"].queryset = User.objects.filter(groups__name='trainers')
    form.fields["athlets"].queryset = User.objects.filter(groups__name='sportsman')

    context = {
        'form' : form,
    }
    return render(request, 'eventHandler/compound.html', context)

def organizationСreate(request):
    if request.method == "POST":
        form = createOrganization(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/event')
    else:
        form = createOrganization()

    context = {
        'form' : form,
    }
    return render(request, 'eventHandler/organizationCreate.html', context)


def createEvent(request):
    if request.method == "POST":
        form = createEventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/event')
    else:
        form = createEventForm()

    form.fields["persons"].queryset = User.objects.filter(groups__name='sportsman')

    context = {
        'form' : form,
    }
    return render(request, 'eventHandler/eventCreate.html', context)

# def appoinTrainer(request):
#     if request.method == "POST":
#         form = createEventForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/event')
#     else:
#         form = createEventForm()
#
#     context = {
#         'form' : form,
#     }
#     return render(request, 'eventHandler/appointTrainer.html', context)

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