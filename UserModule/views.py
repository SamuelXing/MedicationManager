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
    if u.id == request.user.id:
        userInfo = NormalUser.objects.get(nickname = u.username)
        userInfo.user = u
        return render_to_response('User/user-info.html', {'request':request, 'userInfo': userInfo, 'user': u })
    else:
        userInfo = NormalUser.objects.get(nickname = u.username)
        userInfo.user = u
        return render_to_response('User/user-public-info.html', {'request': request, 'userInfo': userInfo, 'user': u })
