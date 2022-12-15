from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User

class createSportType(ModelForm):
    class Meta:
        model = SportType
        fields = ['name', 'custom']

class createTeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['name']
        widgets = {
            'name' : forms.TextInput(),
        }

class createSportObject(ModelForm):
    class Meta:
        model =  SportObject
        fields = ['name', 'address']

class createEventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'status', 'owner', 'settings']
        widgerts = {
            'name' : forms.TextInput(),
        }

class createSportTypeEvent(ModelForm):
    class Meta:
        model = SportTypeEvent
        fields = ['date', 'time', 'sport_object', 'sport_type']

class appoinTrainerForm(forms.Form):
    names = forms.ModelMultipleChoiceField(queryset = User.objects.filter(groups__name='sportsman'))