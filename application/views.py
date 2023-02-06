from django.shortcuts import render
from django.http import HttpResponse
from application.models import Shoppinglist, Item, Malllist, UserList

# Create your views here.


def index(request):
    user_list = UserList.objects.first(user_id=1)
    result = Shoppinglist.objects.filter(list_id=user_list.list_id)
    new_result = [item.__dict__ for item in result]
    return HttpResponse(str(new_result))


def add_item(request):
    return HttpResponse("Add Item")


def buy_item(request, item_id):
    return HttpResponse("Buy Item")


def remove_item(request, item_id):
    return HttpResponse("Remove Item")


def index_user(request):
    return HttpResponse("Index User")


def add_shop(request):
    return HttpResponse("Add Shop")


def add_user(request):
    return HttpResponse("Add User")


def analytics(request):
    return HttpResponse("Analytics")

