from django.shortcuts import render
from django.http import HttpResponse
from application.models import Shoppinglist, Item, Malllist, UserList

# Create your views here.


def index(request):
    if request.method == 'POST':
        item_name = request.POST.get('item')
        quantity = request.POST.get('quantity')
        shop_id = request.POST.get('shop')
        shop_object = Malllist.objects.filter(id=shop_id).first()
        item_object = Item(name=item_name, shop_id=shop_object)
        shoppinglist_object = Shoppinglist(item_id=item_object, quantity=quantity)
        item_object.save()
        shoppinglist_object.save()
    user_list = UserList.objects.first(user_id=1)
    result = Shoppinglist.objects.filter(list_id=user_list.list_id)
    new_result = [item.__dict__ for item in result]
    return render(request, 'item_list.html',
                  {'shoppinglist_data': new_result,
                   'shops': Malllist.objects.all().filter(list_id=user_list.list_id)})


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

