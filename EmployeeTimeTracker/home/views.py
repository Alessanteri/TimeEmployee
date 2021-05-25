from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users, admin_only
from loginmanager.models import *
from django.utils.translation import gettext as _
# Create your views here.


@login_required(login_url='loginmanager-login')
# @allowed_users(allowed_roles=['Admin', 'Subadmin'])
@admin_only
def home(request):
    # return HttpResponse('This is home page')
    userinfo = Profile.objects.filter(user_id=request.user.id)
    context = {'userinfo': userinfo}
    return render(request, 'home/index.html', context)


def userPage(request):
    # return HttpResponse('This is home page')
    context = {
        'hello': _('Hello')
    }
    return render(request, 'home/user.html', context)
