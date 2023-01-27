from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views.generic import DetailView, DeleteView, UpdateView
from django.contrib.auth.models import Group, User
from django.forms import formset_factory
from .utils import *

# Create your views here.
def myEvent(request):
    eventNameList = Event.objects.filter(owner=request.user.pk)
    context = {
        'title': 'Список моих мероприятий',
        'events' : eventNameList,
    }
    return render(request, 'eventHandler/event.html', context)

def allSportsmans(request):
    sportsmanList = AuthUser.objects.all() #.filter(groups__name='sportsman')
    context = {
        'title' : 'Список всех спортсменов',
        'sportsmans' : sportsmanList,
    }
    return render(request, 'eventHandler/sportsmans.html', context)

def mySportsmans(request):
    sportsmanList = AuthUser.objects.filter(groups__name='sportsman', place_employment=request.user.place_employment)
    context = {
        'title': 'Список моих спортсменов',
        'sportsmans' : sportsmanList,
    }
    return render(request, 'eventHandler/sportsmans.html', context)

def allEvents(request):
    eventNameList = Event.objects.all()
    context = {
        'title': 'Список всех мероприятий',
        'events': eventNameList,
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
        'title': 'Создание вида спорта',
        'form' : form,
    }
    return render(request, 'eventHandler/sportCreate.html', context)

def sportObjectCreate(request):
    if request.method == "POST":
        form = createSportObject(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/event')
    else:
        form = createSportObject()

    context = {
        'title': 'Создание спортивного обьекта',
        'form' : form,
    }
    return render(request, 'eventHandler/sportObjectCreate.html', context)

def SportTypeEventcreate(request):
    if request.method == "POST":
        if request.POST.get("send"):
            form = form(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/event')

    else:
        form = formset_factory(createSportTypeEvent, extra=1) #, can_delete=True

    context = {
        'form': form,
    }
    return render(request, 'eventHandler/SportTypeEventcreate.html', context)

def createEvent(request):
    if request.method == "POST":
        form = createEventForm(request.user, request.POST)
        if form.is_valid():
            ptype = form.save(commit=False)
            ptype.owner = request.user
            ptype.save()
            return redirect('/event')
    else:
        form = createEventForm(request.user)

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

class profile(UpdateView):
    model = AuthUser
    template_name = 'eventHandler/profile.html'
    form_class = userEdit

# class eventUpdate(UpdateView):
#     model = Event
#     template_name = 'eventHandler/eventUpdate.html'
#     form_class = createEventForm
#
# class eventDelete(DeleteView):
#     model = Event
#     success_url = '/event'
#     template_name = 'eventHandler/eventDelete.html'
