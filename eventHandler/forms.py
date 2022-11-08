from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User

member = (
    ('Антон','Антон'),
    ('Паша', 'Паша'),
    ('Вика', 'Вика'),
    ('Кирилл', 'Кирилл'),
)

class createEventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'person', 'time']
        widgerts = {
            'name' : forms.TextInput(),
            'date' : forms.DateField(),
            'person' : forms.MultipleChoiceField(choices= member),
            'time' : forms.TimeField(),
        }

class createTeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'trainer', 'athletes']
        widgerts = {
            'name' : forms.TextInput(),
        }

    # def __init__(self, user=None, **kwargs):
    #     super(createTeamForm, self).__init__(**kwargs)
    #     self.fields['trainer'].queryset = User.objects.filter(groups__name='trainers')
    #     self.fields['athletes'].queryset = User.objects.filter(groups__name='sportsman')