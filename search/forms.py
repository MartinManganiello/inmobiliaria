from django import forms


class OrderForm(forms.Form):
    TYPE_CHOICES = [
        ("1", "Nuevos"),
        ("2", "Alquiler"),
        ("3", "Venta"),
    ]

    order_by = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.Select())
