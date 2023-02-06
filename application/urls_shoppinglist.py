from django.urls import path
from . import views

urlpatterns = [
    path('/', views.index, name='index'),
    path('add/', views.add_item, name='add_item'),
    path('<item_id>/buy', views.add_item, name='buy_item'),
    path('<item_id>/remove', views.add_item, name='remove_item'),
]


