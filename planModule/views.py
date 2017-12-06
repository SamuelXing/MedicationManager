from .models import Plan, Drug
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, render
from django.contrib.auth.decorators import login_required
from django.template import  RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .planForm import PlanForm
from django.contrib import messages



# Create your views here.
# TODO: response messages
@login_required
def addAPlan(request):
    if request.method == 'GET':
        drugs = Drug.objects.all()
        form = PlanForm()
        return render(request, 'Plan/create.html', {'form': form, 'drugs': drugs})
    elif request.method == 'POST':
        name = request.POST.get('name')
        user_id = request.user.id
        drug_name = request.POST.get('drug')
        frequencies = request.POST.get('frequencies')
        dose = request.POST.get('dose')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')

        if not User.objects.filter(pk = user_id).exists():
            messages.add_message(request, messages.WARNING, "username does not exist")
            return HttpResponseRedirect(reverse('plan:plan_create'))

        user = User.objects.get(pk = user_id)
        drug = Drug.objects.get(name = drug_name)

        newPlan = Plan()
        newPlan.name = name
        newPlan.user=User.objects.get(id=user_id)
        newPlan.drug=Drug.objects.get(name=drug)
        newPlan.frequencies=frequencies
        newPlan.does=dose
        newPlan.startDate=startDate
        newPlan.endDate=endDate
        newPlan.save()
        plans = get_list_or_404(Plan, user__pk = request.user.id)
        return render_to_response('Plan/lists.html',locals(), context_instance = RequestContext(request))



@login_required
def editAPlan(request, plan_id):
    if request.method == 'GET':
        plan = get_object_or_404(Plan, pk = plan_id)
        drugs=Drug.objects.all()
        form = PlanForm()
        return render_to_response('Plan/edit.html', locals(), context_instance = RequestContext(request))

    elif request.method == 'POST':
        instance=get_object_or_404(Plan,id=plan_id)
        form = PlanForm(request.POST or None,instance=instance)
        if form.is_valid():
            newPlan = form.save(commit=False)
            newPlan.user = request.user
            drug_name = request.POST.get('drug')
            drug = Drug.objects.get(name = drug_name)
            newPlan.drug=Drug.objects.get(name=drug)
            newPlan.frequencies=request.frequencies
            newPlan.does=request.dose
            newPlan.startDate=request.startDate
            newPlan.endDate=request.endDate
            newPlan.save()
            plans = get_list_or_404(Plan, user__pk = request.user.id)
            return render_to_response('Plan/lists.html',locals(), context_instance = RequestContext(request))
        else:
            return HttpResponseRedirect(reverse('plan:plan_edit', args=(plan_id,)))


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
        userid = request.user.id
        plans = Plan.objects.filter(user__pk = userid)
        return render_to_response('Plan/lists.html', locals(), context_instance = RequestContext(request))


