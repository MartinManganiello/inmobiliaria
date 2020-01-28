from django import forms
from .models import Estate


class AutoForm(forms.Form):
    TYPE_CHOICES = [
        ("1", "Nuevos"),
        ("2", "Alquiler"),
        ("3", "Venta"),
    ]

    order_by = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.Select(
        attrs={'onchange': 'get_order();'}))
