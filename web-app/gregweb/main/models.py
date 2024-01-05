from django.db import models

# Create your models here.
class Products(models.Model):
    objects = None
    name_products = models.CharField('Название', max_length=30)
    price_products = models.IntegerField('Цена')
    description_products = models.TextField('Описание', max_length=250)
    description_products_min = models.CharField('Описание краткое', max_length=50)
    numb_photo = models.TextField('Нумерация фото', max_length=20)

    def __str__(self):
        return self.name_products

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class ProductBasket(models.Model):
    objects = None
    session_key = models.CharField('Ключ сессии', max_length=128, default=None)
    name_products = models.CharField('Название', max_length=30, default=None)
    price_products = models.IntegerField('Цена', default=None)
    count_products = models.IntegerField('Количество', max_length=250, default=None)
    description_products = models.CharField('Краткое описание ', max_length=50, default=None)
    numb_photo = models.CharField('Нумерация фото', max_length=20, default=None)

    def __str__(self):
        return self.name_products

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'
