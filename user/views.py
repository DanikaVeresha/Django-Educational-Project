from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def index(request):
    return HttpResponse("User")


def user_login(request):
    if request.user.is_authenticated:
        return HttpResponse("User already logged in")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/shoppinglist')
        else:
            return redirect('/user/register')
    else:
        return render(request, 'login.html')


def user_register(request):
    if request.user.is_authenticated:
        return HttpResponse("User already logged in")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect('/user/login')
    return render(request, 'register.html')


def user_logout(request):
    logout(request)
    return redirect('/user/login')

