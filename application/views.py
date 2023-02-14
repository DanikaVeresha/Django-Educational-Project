from django.shortcuts import render
from django.http import HttpResponse
from application.models import Shoppinglist, Item, Malllist, UserList

# Create your views here.


def index(request):
    user_list = UserList.objects.filter(id=1).first()
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
    user_list = UserList.objects.filter(id=1).first()
    if request.method == 'POST':
        item_id = request.POST.get('item')
        item_object = Item.objects.filter(pk=int(item_id)).first()
        shoppinglist_obj = Shoppinglist.objects.filter(item_id=item_object).first()
        shoppinglist_obj.status = 'bought'
        shoppinglist_obj.save()
    result = Shoppinglist.objects.filter(list_id=user_list.list_id)
    return render(request, 'buy_item.html',
                  {'shoppinglist_data': result,
                   'items': Item.objects.all().filter(shop_id__list_id=user_list.list_id)})


def remove_item(request, item_id):
    user_list = UserList.objects.filter(id=1).first()
    if request.method == 'POST':
        item_id = request.POST.get('item')
        item_object = Item.objects.filter(pk=int(item_id)).first()
        item_obj = Item.objects.filter(id=item_object.id).first()
        item_obj.delete()
    result = Shoppinglist.objects.filter(list_id=user_list.list_id)
    return render(request, 'remove_item.html',
                  {'shoppinglist_data': result,
                   'items': Item.objects.all().filter(shop_id__list_id=user_list.list_id)})


def index_user(request):
    return HttpResponse("Index User")


def add_shop(request):
    return HttpResponse("Add Shop")


def add_user(request):
    return HttpResponse("Add User")


def analytics(request):
    return HttpResponse("Analytics")

