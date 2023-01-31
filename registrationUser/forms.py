from django import forms
from django.contrib.auth.forms import UserCreationForm
from eventHandler.models import Account

class customCreateUser(UserCreationForm):
    class Meta:
        model = Account
        fields = ('username', 'password1', 'password2')
