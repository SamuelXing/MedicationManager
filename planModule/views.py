from .models import Plan, Drug
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, render
from django.contrib.auth.decorators import login_required
from django.template import  RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .planForm import PlanForm


# Create your views here.
@login_required
def addAPlan(request):
    if request.method == 'GET':
        drugs = Drug.objects.all()
        form = PlanForm()
        return render(request, 'Plan/create.html', {'form': form, 'drugs': drugs})
    elif request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            newPlan = form.save(commit=False)
            newPlan.user = request.user
            newPlan.save()
            return HttpResponseRedirect(reverse('plan:plan_lists'))
        else:
            return HttpResponseRedirect(reverse('plan:plan_create'))


@login_required
def editAPlan(request, plan_id):
    if request.method == 'GET':
        plan = get_object_or_404(Plan, pk = plan_id)
        form = PlanForm(instance=plan)
        return render(request, 'Plan/edit.html', {'form': form})
    elif request.method == 'POST':
        form = PlanForm(request.POST)
        if form.is_valid():
            newPlan = form.save(commit=False)
            newPlan.user = request.user
            newPlan.save()
            return HttpResponseRedirect(reverse('plan:plan_detail', args=(newPlan.id), ))
        else:
            return HttpResponseRedirect(reverse('plan:plan_edit'))


@login_required
def dropAPlan(request, plan_id):
    if request.method == 'POST':
        Plan.objects.filter(id = plan_id).delete()
        return HttpResponseRedirect(reverse('plan:plan_lists'))


@login_required
def detail(request, plan_id):
    if request.method == 'GET':
        plan = get_object_or_404(Plan, pk = plan_id)
        return render_to_response('Plan/detail.html', locals(), context_instance = RequestContext(request))


@login_required
def listPlans(request):
    if request.method == 'GET':
        plans = get_list_or_404(Plan, user__pk = request.user.id)
        return render_to_response('Plan/lists.html', locals(), context_instance = RequestContext(request))

