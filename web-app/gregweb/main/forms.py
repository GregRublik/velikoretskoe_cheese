from .models import ProductBasket
from django.forms import ModelForm, TextInput, NumberInput


class ProductBasketForm(ModelForm):
    class Meta:
        model = ProductBasket
        fields = ['session_key', 'name_products', 'price_products', 'count_products', 'description_products',
                  'numb_photo']
        widgets = {
            'session_key': TextInput(attrs={
                'value': '{{SES_KEY}}',
                'name': 'session_key',
                'id': 'session_key_{{el.numb_photo}}',

            }),
            'name_products': TextInput(attrs={
                'value': '{{el.name_products}}',
                'name': "name_products",
                'id': 'name_products_{{el.numb_photo}}',

            }),
            'price_products': NumberInput(attrs={
                'value': '{{el.price_products}}',
                'name': "price_products",
                'id': 'price_products_{{el.numb_photo}}',

            }),
            'count_products': NumberInput(attrs={
                'name': "number",
                'type': "number",
                'id': "number_{{el.numb_photo}}",
                'class': "form-control",
                'placeholder': "Укажите вес (гр)",
                'style': "width: 37%;",

            }),
            'description_products': TextInput(attrs={
                'value': "{{ el.description_products_min }}",
                'name': "description_products",
                'id': 'description_products_{{el.numb_photo}}',

            }),
            'numb_photo': TextInput(attrs={
                'value': '{{el.numb_photo}}',
                'name': "product_id",
                'id': 'numb_photo_{{el.numb_photo}}',

            })

        }
