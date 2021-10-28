from django.contrib import admin, messages
from . import models
from . import forms


@admin.register(models.Products)
class Products_admin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'quantity',
    )


@admin.register(models.Orders)
class Orders_admin(admin.ModelAdmin):
    list_display = (
        'order_no',
        'name',
        'status',
        'created_at',
    )
    exclude = (
        'order_no',
    )

    def name(self, obj):
        return '{} {}'.format(obj.client.first_name, obj.client.last_name)


@admin.register(models.Order_line)
class Order_line_admin(admin.ModelAdmin):
    list_display = (
        'line_id',
        'order_no',
        'product_name',
        'product_price',
        'quantity',
        'total_price',
    )
    exclude = (
        'line_id',
    )
    form = forms.OrderLineAdminForm

    def order_no(self, obj):
        return obj.order.order_no

    def product_name(self, obj):
        return obj.product.name

    def product_price(self, obj):
        return obj.product.price

    def total_price(self, obj):
        return obj.product.price * obj.quantity

    def save_model(self, request, obj, form, change):
        return super().save_model(request, obj, form, change)
