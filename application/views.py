
import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from application.models import Shoppinglist, Item, Malllist, UserList

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect('/user/login')
    user_id = request.user.id
    user_list = UserList.objects.filter(id=user_id).first()
    if request.method == 'POST':
        item_name = request.POST.get('item')
        price = request.POST.get('price')
        shop_id = request.POST.get('shop')
        shop_object = Malllist.objects.filter(pk=int(shop_id)).first()
        item_object = Item(name=item_name, shop_id=shop_object)
        item_object.save()
        shoppinglist_object = Shoppinglist(
            list_id=user_list.list_id,
            item_id=item_object,
            price=price)
        shoppinglist_object.save()
    result = Shoppinglist.objects.filter(list_id=user_list.list_id)
    return render(request, 'item_list.html',
                  {'shoppinglist_data': result,
                   'shops': Malllist.objects.all().filter(list_id=user_list.list_id),
                   'items': Item.objects.all().filter(shop_id__list_id=user_list.list_id)})


def buy_item(request, item_id):
    if not request.user.is_authenticated:
        return redirect('/user/login')
    if request.method == 'POST':
        item_id = request.POST.get('item')
        item_object = Item.objects.filter(pk=int(item_id)).first()
        shoppinglist_obj = Shoppinglist.objects.filter(item_id=item_object).first()
        shoppinglist_obj.status = 'bought'
        shoppinglist_obj.buy_date = datetime.datetime.now()
        shoppinglist_obj.save()
    return redirect('/shoppinglist')


def remove_item(request, item_id):
    if not request.user.is_authenticated:
        return redirect('/user/login')
    if request.method == 'POST':
        item_id = request.POST.get('item')
        item_object = Item.objects.filter(pk=int(item_id)).first()
        item_obj = Item.objects.filter(id=item_object.id).first()
        item_obj.delete()
    return redirect('/shoppinglist')


def add_shop(request):
    if not request.user.is_authenticated:
        return redirect('/user/login')
    user_id = request.user.id
    user_list = UserList.objects.filter(id=user_id).first()
    if request.method == 'POST':
        shop_name = request.POST.get('shop')
        malllist_object = Malllist(name=shop_name, list_id=user_list.list_id)
        malllist_object.save()
    result = Shoppinglist.objects.filter(list_id=user_list.list_id)
    return render(request, 'item_list.html',
                  {'shoppinglist_data': result,
                   'shops': Malllist.objects.all().filter(list_id=user_list.list_id),
                   'items': Item.objects.all().filter(shop_id__list_id=user_list.list_id)})


def analytics(request):
    return HttpResponse("Analytics")





