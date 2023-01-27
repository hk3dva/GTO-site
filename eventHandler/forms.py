from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User

class userEdit(ModelForm):
    class Meta:
        model = AuthUser
        fields = ['first_name', 'last_name', 'birthday_date', 'photo', 'place_employment', 'gto_id']

class createSportType(ModelForm):
    class Meta:
        model = SportType
        fields = ['name', 'custom', 'for_who']

class createTeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['name' , 'count']
        widgets = {
            'name' : forms.TextInput(),
        }

class createSportObject(ModelForm):
    class Meta:
        model =  SportObject
        fields = ['name', 'address', 'photo']

class createEventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'status', 'settings', 'min_age', 'max_age', 'photo']
        widgerts = {
            'name' : forms.TextInput(),
        }

    def __init__(self, user, *args, **kwargs):
        super(createEventForm, self).__init__(*args, **kwargs)
        self.owner = user


class createSportTypeEvent(ModelForm):
    class Meta:
        model = SportTypeEvent
        fields = ['date', 'time', 'sport_object', 'sport_type', 'sportsmans']

class appoinTrainerForm(forms.Form):
    names = forms.ModelMultipleChoiceField(queryset = User.objects.filter(groups__name='sportsman'))