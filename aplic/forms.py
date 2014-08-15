from django import forms
from aplic.models import *
class DataInput(forms.Form):
    file = forms.FileField()
    place = forms.ModelChoiceField(queryset=Persona.objects.all())
