from django import forms

from .models import Drug

class AddDrugForm(forms.Form):
    name = forms.CharField(max_length=100,
                           error_messages={
                               'required': "Drug's name cannot be none",
                               'max_length': "name cannot exceed 100 characters"
                           })
    description = forms.CharField(max_length=500,)
    toxicity = forms.CharField(max_length=200,)
    interactions = forms.CharField(max_length=200, )
