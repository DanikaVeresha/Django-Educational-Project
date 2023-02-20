from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import uuid
from application.models import UserList


def index(request):
    return HttpResponse("User")


def user_invate(request):
    if not request.user.is_authenticated:
        return redirect('/user/login')
    if request.method == 'GET':
        return render(request, 'invate_user.html')
    email = request.POST.get('email')
    invated_user = User.objects.filter(email=email).first()
    if invated_user is None:
        return HttpResponse("User not found")
    invated_user_list = UserList.objects.filter(id=invated_user.id).first()
    user_list = UserList.objects.filter(id=request.user.id).first()
    invated_user_list.list_id = user_list.list_id
    invated_user_list.save()
    return HttpResponse(f"User {invated_user.email} invated")


def user_login(request):
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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create_user(username, email, password)
        user.save()
        user_list = UserList(id=user.id, list_id=uuid.uuid4())
        user_list.save()
        return redirect('/user/login')
    return render(request, 'register.html')


def user_logout(request):
    logout(request)
    return redirect('/user/login')


