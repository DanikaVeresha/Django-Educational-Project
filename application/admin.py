from django.contrib import admin
from .models import Shoppinglist, Item, Malllist, UserList

# Register your models here.

admin.site.register(Shoppinglist)
admin.site.register(Item)
admin.site.register(Malllist)
admin.site.register(UserList)
