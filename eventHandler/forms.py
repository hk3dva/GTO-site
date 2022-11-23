from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User

class createSportType(ModelForm):
    class Meta:
        model = TypeSport
        fields = ['name']

class createCompound(ModelForm):
    class Meta:
        model = Compound
        fields = ['athlets', 'trainers']

class createOrganization(ModelForm):
    class Meta:
        model = Organization
        fields = ['name']

class createSportObject(ModelForm):
    class Meta:
        model =  SportObject
        fields = ['name', 'place', 'type_sport', 'owner']

class createUserResult(ModelForm):
    class Meta:
        model =  UserResult
        fields = ['user', 'result', 'sport_type']

class createEventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'time', 'type_sport', 'teams', 'persons']
        widgerts = {
            'name' : forms.TextInput(),
            'date' : forms.DateInput(),
            'time' : forms.TimeInput(),
        }

class createTeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'compound']
        widgets = {
            'name' : forms.TextInput(),
        }

# class appoinTrainerForm(Form):
#     name = forms.