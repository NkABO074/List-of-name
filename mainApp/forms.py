from django import forms
from .models import Dudes

class DudesForm(forms.ModelForm):    
    class Meta:
        model = Dudes
        fields = '__all__'

class DudesSearchForm(forms.ModelForm):
    query = forms.CharField(max_length=100, label='Search')
        