from django import forms

member = (
    ('Антон', 'Антон'),
    ('Паша', 'Паша'),
    ('Вика', 'Вика'),
)

class createEventForm(forms.Form):
    name = forms.CharField()
    date = forms.DateField()
    time = forms.TimeField()
    members =   forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices = member)