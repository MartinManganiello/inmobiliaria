from django import forms
from search.models import Estate


class OrderForm(forms.Form):
    TYPE_CHOICES = [
        ("1", "Nuevos"),
        ("2", "Alquiler"),
        ("3", "Venta"),
    ]

    order_by = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.Select())


class SearchForm(forms.Form):
    room = forms.IntegerField(max_value=6, min_value=1)
    garage = forms.IntegerField(max_value=4, min_value=0)
    bathroom = forms.IntegerField(max_value=4, min_value=1)
    city = forms.ChoiceField(choices=Estate.VALID_PROVINCES)
    transaction_type = forms.ChoiceField(choices=Estate.TRANSACTION_TYPE)
