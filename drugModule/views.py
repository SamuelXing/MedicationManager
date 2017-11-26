from django.shortcuts import render
from .models import Drug
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import  RequestContext
from .drugForm import AddDrugForm
from django.contrib.auth.models import User


# Create your views here.
@login_required
def addDrug(request):
    form = AddDrugForm(request.POST)
    if form.is_valid():
        pass


@login_required()
def deleteDrug(request):
    pass



