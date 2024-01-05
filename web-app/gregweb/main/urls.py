from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('catalog', views.catalog, name='catalog'),
    path('contacts', views.contacts, name='contacts'),
    path('basket', views.basket, name='basket'),
    path('confirm', views.confirm, name='confirm'),
    path('confirmed', views.confirmed, name='confirmed'),
    path('login', views.login, name='login'),

]
