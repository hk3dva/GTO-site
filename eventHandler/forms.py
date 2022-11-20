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
        widgets = {
            'name' : forms.TextInput(),
            'date' : forms.DateInput(),
            'time' : forms.TimeInput(),
        }

class createUser(ModelForm):
    class Meta:
        model = AuthUser
        fields = ['username', 'password', 'email', 'first_name', 'last_name', 'birthday_date']
        widgets = {
            'birthday_date': forms.DateInput(),
            'password': forms.PasswordInput()
        }

class createTeamForm(ModelForm):
    # treners =  forms.ModelMultipleChoiceField(
    #     queryset=User.objects.filter(groups__name='trainers'),
    #     widget=forms.CheckboxSelectMultiple())
    # athletes = forms.ModelMultipleChoiceField(
    #     queryset=User.objects.filter(groups__name='sportsman'),
    #     widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Team
        fields = ['name', 'compound']
        widgets = {
            'name' : forms.TextInput(),
        }

    # def __init__(self, *args, **kwargs):
    #     super(createTeamForm, self).__init__(*args, **kwargs)
    #     self.fields['treners'].queryset = User.objects.filter(groups__name='trainers')
    #     self.fields['athletes'].queryset = User.objects.filter(groups__name='sportsman')
#
# def createTrainerTeamForm(ModelForm):
#     class Meta:
#         model = Compound
#         fields = ['trainer', 'students']