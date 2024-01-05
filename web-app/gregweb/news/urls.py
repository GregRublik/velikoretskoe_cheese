from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('create', views.create, name='create'),
    # path('catalog', views.news_catalog, name='catalog'),
    # path('contacts', views.news_contacts, name='contacts'),
    # path('basket', views.news_basket, name='basket')
]
