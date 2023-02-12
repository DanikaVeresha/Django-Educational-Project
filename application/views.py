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
        item_id_status = Shoppinglist.objects.filter(pk=int(item_id)).first()
        item_id_status.status = 'bought'
        item_id_status.save()
    item_status = Shoppinglist.objects.filter(list_id=user_list.list_id)
    return render(request, 'item_list.html',
                  {'item_status': item_status,
                   'shops': Malllist.objects.all().filter(list_id=user_list.list_id),
                   'items': Item.objects.all().filter(shop_id__list_id=user_list.list_id)})


def remove_item(request, item_id):
    user_list = UserList.objects.filter(id=1).first()
    if request.method == 'POST':
        item_remove = Item.objects.filter(pk=int(item_id)).first()
        item_remove.delete()
        itemshoplist_remove = Shoppinglist.objects.filter(item_id=item_remove).first()
        itemshoplist_remove.delete()
    item_delete = Item.objects.filter(shop_id__list_id=user_list.list_id)
    itemshoplist_delete = Shoppinglist.objects.filter(list_id=user_list.list_id)
    return render(request, 'item_list.html',
                  {'item_delete': item_delete,
                   'itemshoplist_delete': itemshoplist_delete,
                   'shops': Malllist.objects.all().filter(list_id=user_list.list_id),
                   'items': Item.objects.all().filter(shop_id__list_id=user_list.list_id)})


def index_user(request):
    return HttpResponse("Index User")


def add_shop(request):
    return HttpResponse("Add Shop")


def add_user(request):
    return HttpResponse("Add User")


def analytics(request):
    return HttpResponse("Analytics")

