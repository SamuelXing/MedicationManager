from django.shortcuts import render
from .models import Drug
from django.shortcuts import render_to_response, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import  RequestContext
from .drugForm import AddDrugForm
from django.contrib.auth.models import User


# Create your views here.
@login_required
def addDrug(request):
	if request.method=='GET':
		drugs=Drug.objects.all()
		if drugs is not None:
			form=AddDrugForm()
			return render(request,"Medication/addDrug.html",{'form':form,'drugs':drugs})
		else:
			return HttpResponse("no drugs yet, please go to admin")
	elif request.method=='POST':
		name=request.POST.get('name')
		description=request.POST.get('description')
		toxicity=request.POST.get('toxicity')
		interaction=request.POST.get('interaction')
		newDrug=Drug()
		newDrug.name=name
		newDrug.description=description
		newDrug.toxicity=toxicity
		if interaction!='--':
			newDrug.interaction=Drug.objects.get(name=interaction)		
		newDrug.save()
		drugs=Drug.objects.all()
		return render_to_response('Medication/addDrug.html',locals(),context_instance = RequestContext(request))




@login_required()
def deleteDrug(request):
	if request.method=='POST':
		form=AddDrugForm()
		drugs=Drug.objects.all()
		drug_id=int(request.POST.get('drug_id'))
		drug=Drug.objects.get(id=drug_id)
		drug.delete()
		return render_to_response('Medication/drugLists.html',locals(),RequestContext(request))



@login_required()
def listDrug(request):
	#if request.method=='GET':
	drugs=Drug.objects.all()
	return render_to_response('Medication/drugLists.html',locals(),context_instance = RequestContext(request))

