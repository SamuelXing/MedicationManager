from django import forms

from .models import Drug

class AddDrugForm(forms.Form):
    class Meta:
    	model=Drug
    	fields='__all__'
    	
