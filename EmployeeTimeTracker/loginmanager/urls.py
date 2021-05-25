from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage, name='loginmanager-login'),
    path('register/', views.registerpage, name='loginmanager-register'),
    path('profile/', views.profile, name='profile'),
    path('logout', views.logoutpage, name='logout'),
    path('password/', views.forgotpasswordpage, name='loginmanager-password'),
    path('error401/', views.error401, name='loginmanager-401'),
    path('error404/', views.error404, name='loginmanager-404'),
    path('error500/', views.error500, name='loginmanager-500'),
]
