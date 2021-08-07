from django.urls import path
from . import views

urlpatterns = [
     path('register', views.register, name='register'),
     path('login', views.login, name='login'),
     path('saveuser', views.saveuser, name='saveuser'),
     path('loginuser', views.loginuser, name='loginuser'),
     path('logout', views.logout, name='logout'),

]