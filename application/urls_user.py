from django.urls import path
from . import views

urlpatterns = [
    path('/', views.index_user, name='index_user'),
    path('add_shop/', views.add_shop, name='add_shop'),
    path('add_user/', views.add_user, name='add_user'),
    path('analytics/', views.analytics, name='analytics'),
]