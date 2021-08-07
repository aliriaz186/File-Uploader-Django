from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('upload-files', views.uploadFiles, name='uploadFiles'),
     path('myfiles', views.myfiles, name='myfiles'),
     path(r'^deletefile/(?P<id>\w+)/$', views.deletefile, name='deletefile'),

]