from django.shortcuts import render, redirect
from .forms import *
from .models import *
from .utils import *
from django.views.generic import DetailView, DeleteView, UpdateView
from django.contrib.auth.models import Group
from django.forms import formset_factory

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

    context = {
        'title' : 'Страница создания мероприятия',
        'form' : form,
    }
    return render(request, 'eventHandler/eventCreate.html', context)

def trainerAppoin(request):
    if request.method == "POST":
        form = appoinForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("names")
            for el in name:
                el.groups.clear()
                Group.objects.get(name='trainers').user_set.add(el)
        return redirect('/event')
    else:
        form = appoinForm()

    context = {
        'title' : 'Страница назначения в должность тренера',
        'name': 'Тернер',
        'form' : form,
    }
    return render(request, 'eventHandler/appointTrainer.html', context)

def organizerAppoin(request):
    if request.method == "POST":
        form = appoinForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("names")
            for el in name:
                el.groups.clear()
                Group.objects.get(name='organizers').user_set.add(el)
        return redirect('/event')
    else:
        form = appoinForm()

    context = {
        'title': 'Страница назначения в должность организатора',
        'name' : 'Организатор',
        'form' : form,
    }
    return render(request, 'eventHandler/appointTrainer.html', context)

def myEvent(request):
    eventNameList = Event.objects.filter(owner=request.user.pk)
    context = {
        'title': 'Список моих мероприятий',
        'events' : eventNameList,
    }
    return render(request, 'eventHandler/event.html', context)

def allEvents(request):
    eventNameList = Event.objects.all()
    context = {
        'title': 'Список всех мероприятий',
        'events': eventNameList,
    }
    return render(request, 'eventHandler/event.html', context)

def allSportsmans(request):
    sportsmanList = Account.objects.filter(groups__name='sportsman')
    context = {
        'name': 'спортсменов',
        'title' : 'Список всех спортсменов',
        'sportsmans' : sportsmanList,
    }
    return render(request, 'eventHandler/sportsmans.html', context)

def allSportsmans(request):
    sportsmanList = Account.objects.filter(groups__name='trainers')
    context = {
        'name' : 'Тренеров',
        'title' : 'Список всех тренеров',
        'sportsmans' : sportsmanList,
    }
    return render(request, 'eventHandler/sportsmans.html', context)


def mySportsmans(request):
    sportsmanList = Account.objects.filter(groups__name='sportsman', organization=request.user.organization)
    context = {
        'name': 'моих спортсменов',
        'title': 'Список моих спортсменов',
        'sportsmans' : sportsmanList,
    }
    return render(request, 'eventHandler/sportsmans.html', context)

def EventSettings(request, pk):
    if request.method == "POST":
        form = createEventSettings(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/event')
    else:
        form = createEventSettings()

    context = {
        'form': form,
    }
    return render(request, 'eventHandler/SportTypeEventcreate.html', context)


def  calculator(request):
    return render(request, 'eventHandler/event.html')



def results(request):
    return render(request, 'eventHandler/event.html')


class profile(DetailView):
    model = Account
    template_name = 'eventHandler/profile.html'
    def get_object(self):
        object = super(profile, self).get_object()
        return object

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     context['user'] = Account.objects.filter(pk=self.pk)
    #     return context
