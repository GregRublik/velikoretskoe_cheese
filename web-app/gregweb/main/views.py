from django.shortcuts import render

from .forms import ProductBasketForm
from .models import Products, ProductBasket
import telebot

bot = telebot.TeleBot('')


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def catalog(request):
    error = ''
    form = ProductBasketForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        error = 'Форма заполнена не верно'
    products = Products.objects.all()
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
        session_key = request.session.session_key
    return render(request, 'main/catalog.html', {'products': products, 'SES_KEY': session_key, 'error': error,
                                                 'form': form})


def contacts(request):
    return render(request, 'main/contacts.html')


def basket(request):
    product_in_basket = ProductBasket.objects.all()
    session_key = request.session.session_key
    data_sum = {}

    if request.method == 'POST':
        object_el = request.POST
        for key, value in object_el.items():
            if key == 'id':
                ProductBasket.objects.filter(id=value).delete()

    for product in product_in_basket:
        if product.session_key not in data_sum:
            data_sum[str(product.session_key)] = 0
        x = product.count_products
        y = product.price_products
        sum_products = x * (y/100)
        product.sum = sum_products
        data_sum[str(product.session_key)] += sum_products

    return render(request, 'main/basket.html', {'product_in_basket': product_in_basket, 'SES_KEY': session_key, 'data_sum': data_sum})


def confirm(request):
    product_in_basket = ProductBasket.objects.all()
    session_key = request.session.session_key
    list_products = '\n'

    if request.method == 'POST':
        confirm_elements = request.POST

        for i in confirm_elements:
            if i not in ['csrfmiddlewaretoken', 'confirm_form_name', 'confirm_form_first_name', 'confirm_form_number',
                         'method of obtaining', 'confirm_form_address', 'address_shop','comment']:
                list_products += confirm_elements[i]
                list_products += '\n'

        if confirm_elements['method of obtaining'] == 'Доставка':
            bot.send_message(1027485309, f"Новый заказ: \nИМЯ: {confirm_elements['confirm_form_name']} \
        \nФАМИЛИЯ: {confirm_elements['confirm_form_first_name']} \nНОМЕР: {confirm_elements['confirm_form_number']} \
        \n{confirm_elements['method of obtaining']}: {confirm_elements['confirm_form_address']}\
        \nТОВАРЫ: { list_products }")
        elif confirm_elements['method of obtaining'] == 'Самовывоз':
            bot.send_message(1027485309, f"Новый заказ: \nИМЯ: {confirm_elements['confirm_form_name']} \
        \nФАМИЛИЯ: {confirm_elements['confirm_form_first_name']} \nНОМЕР: {confirm_elements['confirm_form_number']} \
        \n{confirm_elements['method of obtaining']}: {confirm_elements['address_shop']}\
        \nТОВАРЫ: { list_products } \nКОМЕНТАРИЙ: {confirm_elements['comment']}")

        for element in product_in_basket:
            key = element.session_key
            if key == session_key:
                ProductBasket.objects.filter(id=element.id).delete()

        return render(request, 'main/confirmed.html')

    return render(request, 'main/confirm.html', {'product_in_basket': product_in_basket, 'SES_KEY': session_key,})


def confirmed(request):

    return render(request, 'main/confirmed.html')


def login(request):

    return render(request, 'main/login.html')
