from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User

class createEventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'time', 'type_sport']
        widgerts = {
            'name' : forms.TextInput(),
            'date' : forms.DateField(),
            'time' : forms.TimeField(),
        }

class createTeamForm(ModelForm):
    # treners =  forms.ModelMultipleChoiceField(
    #     queryset=User.objects.filter(groups__name='trainers'),
    #     widget=forms.CheckboxSelectMultiple()
    # )
    # athletes = forms.ModelMultipleChoiceField(
    #     queryset=User.objects.filter(groups__name='sportsman'),
    #     widget=forms.CheckboxSelectMultiple()
    # )
    class Meta:
        model = Team
        fields = ['name', 'treners', 'athletes']
        widgets = {
            'name' : forms.TextInput(),
            'treners' : forms.CheckboxSelectMultiple(),
            'athletes' : forms.CheckboxSelectMultiple(),
        }

    # def __init__(self, *args, **kwargs):
    #     super(createTeamForm, self).__init__(*args, **kwargs)
    #     self.fields['treners'].queryset = User.objects.filter(groups__name='trainers')
    #     self.fields['athletes'].queryset = User.objects.filter(groups__name='sportsman')
