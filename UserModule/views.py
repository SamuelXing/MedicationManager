from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse


from django.core.urlresolvers import reverse
from django.core.validators import RegexValidator
from django.utils.translation import ugettext as _
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import password_reset, password_reset_confirm
from planModule.models import Plan


from .models import NormalUser
from django.contrib.auth.models import User

# Create your views here.
alphanumeric = RegexValidator(r'^[0-9a-zA-Z\_]*$', 'Only alphanumeric characters and underscore are allowed.')
emailCheck=RegexValidator(r'^([0-9a-zA-Z\_\.]*?)@([0-9a-zA-Z]*?)\.([0-9a-zA-Z]*?){3}$','Only formal email address is valid.')

@login_required
def user_info(request, user_id):
    u = get_object_or_404(User, pk = user_id)
    if u.is_staff:
        return HttpResponse(u'Sorry, you have no permission to access admin user\'s info')

    userInfo = NormalUser.objects.get(nickname = u.username)
    userInfo.user = u
    return render_to_response('User/user-info.html', {'request':request, 'userInfo': userInfo, 'user': u })

# TODO:redirect
def signup(request):
    if request.method == 'GET':
        return render_to_response('User/signup.html', {}, context_instance = RequestContext(request))
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('password2')

        try:
            alphanumeric(username)
        except:
            messages.add_message(request, messages.WARNING,
                                 "username can only contain letters, numbers, and \'_\'")
            return HttpResponseRedirect(reverse('user:signup'))

        try:
            emailCheck(email)
        except:
            messages.add_message(request, messages.WARNING, 'invaild address')
            return HttpResponseRedirect(reverse('user:signup'))

        if User.objects.filter(username = username).exists():
            messages.add_message(request, messages.WARNING, "username already existed")
            return HttpResponseRedirect(reverse('user:signup'))

        if password != confirm or password == '' or confirm == '':
            messages.add_message(request, messages.WARNING, "password does not match")
            return HttpResponseRedirect(reverse('user:signup'))

        user = User.objects.create_user(username, email, password)
        user = authenticate(username = username, password = password)
        login(request, user)
        p = NormalUser()
        p.user = user
        p.nickname = user.username
        p.save()
        plans = Plan.objects.filter(user__pk=user.id)
        return render_to_response('Plan/lists.html', locals(), context_instance=RequestContext(request))
        return HttpResponseRedirect(reverse('plan:plan_list'))

def signin(request):
    if request.method == 'GET':
        return render_to_response("User/signin.html", context_instance = RequestContext(request))
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password=password)

        if not User.objects.filter(username=username).exists():
            messages.add_message(request, messages.WARNING, "username does not exist")
            return HttpResponseRedirect(reverse('user:signin'))

        if user is None:
            messages.add_message(request, messages.WARNING, "invalid password")
            return HttpResponseRedirect(reverse('user:signin'))

        login(request, user)
        return render_to_response("Medication/homepage.html")

def signout(request):
    logout(request)
    return render_to_response("Medication/homepage.html")

@login_required
def settings(request):
    if request.method == 'GET':
        return render_to_response('User/settings.html', {'request': request},
                                  context_instance = RequestContext(request))
    elif request.method == 'POST':
        u = User.objects.get(username = request.user.username)
        u.email = request.POST['email']

        if request.POST['newPass'] != '' or request.POST['confirmPass'] != '':
            oldPass = request.POST['oldPass']
            newPass = request.POST['newPass']
            if request.POST['newPass'] != request.POST['confirmPass'] or request.POST['newPass'] == '' or \
                            request.POST['confirmPass'] == '':
                messages.add_message(request, messages.WARNING, _('passwords don\'t match, or are blank'))
                return HttpResponseRedirect(reverse('user:change_password'))

            if authenticate(username=u.username, password=oldPass):
                u.set_password(newPass)
                u.save()
                messages.add_message(request, messages.SUCCESS, _('password updated successfully'))
                update_session_auth_hash(request, u)
                return HttpResponseRedirect(reverse('user:settings'))
        else:
            u.save()
            request.user.save()
            return HttpResponseRedirect(reverse('user:settings'))




