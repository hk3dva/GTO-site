from django import forms
from django.forms import ModelForm
from .models import *

class userEdit(ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'birthday_date', 'photo', 'gto_id']

class createSportType(ModelForm):
    class Meta:
        model = SportType
        fields = ['name', 'custom', 'for_who', 'teamable', 'age_max', 'age_min']
        widgerts = {
            'name' : forms.TextInput(attrs={'type' : "text",
                                    'class' : "form-control", 'id' : 'name',
                                    'placeholder' : "Укажите название вида спорта"}),

        }
class createSportObject(ModelForm):
    class Meta:
        model =  SportObject
        fields = ['name', 'address', 'photo', 'city', 'sport_type']

class createTeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['name' , 'count']
        widgets = {
            'name' : forms.TextInput(),
        }

class UserAdd(ModelForm):
    class Meta:
        model = SportTypeEvent
        fields = ['sportsmans', 'sport_type']

class createEventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'age_min', 'age_max', 'photo']
        widgerts = {
            'name' : forms.TextInput(),
        }

    def __init__(self, user, *args, **kwargs):
        super(createEventForm, self).__init__(*args, **kwargs)
        self.owner = user


class createEventSettings(ModelForm):
    class Meta:
        model = SportTypeEvent
        fields = ['date', 'time', 'sport_object', 'sport_type']



class addResultForm(forms.Form):
    sportsman = forms.ModelChoiceField(queryset = Account.objects.all())
    result = forms.CharField()

class appoinForm(forms.Form):
    names = forms.ModelMultipleChoiceField(queryset = Account.objects.all()) # filter(groups__name='sportsman')

class inventoryForm(forms.Form):
    count = forms.IntegerField()
    sport = forms.ModelChoiceField(queryset=SportType.objects.all())