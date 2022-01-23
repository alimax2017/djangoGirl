from django import forms
from .models import Owner, Pet

class IDForm(forms.Form):
    ID_number = forms.IntegerField(label= 'Enter your pet\'s ID number')

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'

class PetForm(forms.ModelForm):
    class Meta:
        Model=Pet
        fields='__all__'


