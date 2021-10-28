from django import forms
from django.forms.models import ModelForm
from app_orders import models


class OrdersForm(ModelForm):
    class Meta:
        model = models.Orders
        fields = '__all__'

    status = forms.CharField(
        label='Status',
        max_length=100,
        required=False,
    )
    client = forms.ModelChoiceField(
        queryset=models.User.objects.all(),
        required=True
    )


class OrderLineForm(ModelForm):
    class Meta:
        model = models.Order_line
        fields = '__all__'

    quantity = forms.FloatField(
        label='Quantity',
        required=True,
    )
    product = forms.ModelChoiceField(
        label='Product',
        queryset=models.Products.objects.all(),
        required=True
    )
    order = forms.ModelChoiceField(
        label='Order',
        queryset=models.Orders.objects.all(),
        required=True
    )
