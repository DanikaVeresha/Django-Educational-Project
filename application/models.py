from django.db import models

# Create your models here.


class Shoppinglist(models.Model):
    list_id = models.UUIDField()
    item_id = models.ForeignKey('Item', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.CharField(default='available', max_length=20)
    buy_date = models.DateField()


class UserList(models.Model):
    user_id = models.IntegerField()
    list_id = models.UUIDField()


class Malllist(models.Model):
    name = models.CharField(max_length=100)
    list_id = models.UUIDField()


class Item(models.Model):
    name = models.CharField(max_length=100)
    shop_id = models.ForeignKey(Malllist, on_delete=models.CASCADE)

