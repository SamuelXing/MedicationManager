from django.forms import ModelForm
from .models import Plan

class PlanForm(ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'
        exclude = ['user']

