from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                print(request.user.groups.all()[0].name)

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                # return HttpResponse('Restricted User')
                return redirect('loginmanager-401')

            # print('working', allowed_roles)
            # return view_func(request, *args, **kwargs)

        return wrapper_func

    return decorator


def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):

        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'Admin':
            return view_func(request, *args, **kwargs)

        if group == 'Subadmin':
            return view_func(request, *args, **kwargs)

        if group == 'User':
            # return HttpResponse('User Area')
            # return redirect('user-page')
            return view_func(request, *args, **kwargs)

        # print('working', allowed_roles)
        return view_func(request, *args, **kwargs)

    return wrapper_func
