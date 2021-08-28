from utils.helpers import getCleanData
from . import models
from django import forms

class OrderLineAdminForm(forms.ModelForm):
    class Meta:
        model = models.Orders
        fields = '__all__'

    def clean(self):
        data = getCleanData(self, ['order', 'product', 'quantity'])
        if not data['order'] or not data['product']:
            raise forms.ValidationError(
                u"Please select order and product!"
            )
        quantity = float(data['quantity'])
        if quantity <= 0.0:
            raise forms.ValidationError(
                u"Quantity should be greater than zero!"
            )
        if quantity > data['product'].quantity:
            raise forms.ValidationError(
                u"Quantity should be greater than Product Stock!"
            )
        return self.cleaned_data
