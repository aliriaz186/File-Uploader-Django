from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from authapp.models import User
from django.contrib import messages
from django.contrib.auth.models import auth

# Create your views here.
def register(request):
    return render(request, 'registration.html')
def login(request):
    return render(request, 'login.html')
def saveuser(request):
    name = request.POST['name']
    email = request.POST['email']
    password = request.POST['password']
    if name == '' or email == '' or password == '':
        messages.info(request, 'Invalid inputs')
        return redirect('register')
    user = User()
    user.name = name
    user.email = email
    user.password = password
    user.save()
    return redirect('login')

def loginuser(request):
    email = request.POST['email']
    password = request.POST['password']
    if email == '' or password == '':
        messages.info(request, 'Invalid email or password')
        return redirect('login')
    userCount = User.objects.filter(email=email, password=password).count()
    if userCount is not 0:
        user = User.objects.get(email=email, password=password)
        request.session['userId'] = user.id
        return redirect('/')
    else:
        messages.info(request, 'Invalid email or password')
        return redirect('login')
def logout(request):
    if 'userId' in request.session:
        del request.session['userId']
    return redirect('login')