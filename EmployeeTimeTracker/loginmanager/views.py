from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib import messages
from .decorators import unauthenticated_user, admin_only
from .forms import CreateUserForm, ProfileForm
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.


@unauthenticated_user
def loginpage(request):
    # if request.user.is_authenticated:
    #     return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Wrong Username or Password')

    context = {}
    return render(request, 'loginmanager/login.html', context)
    # return HttpResponse('Login home page')


def logoutpage(request):
    logout(request)
    return redirect('home')


# @unauthenticated_user
def registerpage(request):
    # if request.user.is_authenticated:
    #     return redirect('home')

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='Users')
            user.groups.add(group)

            messages.success(request, 'Account was сreated for ' + username + ".")
            return redirect('home')
        else:
            messages.error(request, 'Account not created.')
            return redirect('loginmanager-register')

    else:
        form = CreateUserForm()
        context = {'form': form}
        return render(request, 'loginmanager/register.html', context)


def forgotpasswordpage(request):
    return render(request, 'loginmanager/password.html')


def error401(request):
    return render(request, 'loginmanager/401.html')


def error404(request):
    return render(request, 'loginmanager/404.html')


def error500(request):
    return render(request, 'loginmanager/500.html')


@login_required(login_url='login')
def profile(request):
    user = request.user

    Profilefound = None
    try:
        Profilefound = request.user.profile.user
    except:
        pass

    print(Profilefound)
    if Profilefound is None:
        # print('No profile found')
        form = ProfileForm(instance=user)
    else:
        # print('Profile found')
        profile = request.user.profile
        form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if Profilefound == None:
            if form.is_valid():
                profiledata = form.save(commit=False)
                profiledata.user = request.user
                # print('form is valid')
                profiledata.save()
                # form.save()
                messages.success(request, 'Profile Created Successfully ')
        else:
            form = ProfileForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile Updated Successfully ')

    context = {'form': form}
    return render(request, 'loginmanager/profile.html', context)
