from django.db import models
from django.contrib.auth.models import User
from utils import helpers


class Products(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0.0)
    quantity = models.FloatField(default=0.0)

    class Meta:
        verbose_name_plural = "products"
        ordering = ['-id']
        db_table = "products"

    def __str__(self):
        return '{} ({}) - {}'.format(self.name, self.quantity, self.price)


class Orders(models.Model):
    ORDER_STATUS = (('pending', 'Pending'), ('delivered', 'Delivered'))
    status = models.CharField(
        max_length=100, choices=ORDER_STATUS, default=ORDER_STATUS[0][0])
    order_no = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(User, models.CASCADE)

    class Meta:
        verbose_name_plural = "orders"
        ordering = ['-id']
        get_latest_by = ['id']
        db_table = "orders"

    def __str__(self):
        return '{}'.format(self.order_no)

    def save(self, *args, **kwargs):
        self.order_no = _get_unique_id(self, "OD", "order_no")
        return super().save(*args, **kwargs)


class Order_line(models.Model):
    line_id = models.CharField(max_length=255, null=True, blank=True)
    order = models.ForeignKey(Orders, models.CASCADE)
    product = models.ForeignKey(Products, models.CASCADE)
    quantity = models.FloatField(default=0.0)

    class Meta:
        verbose_name_plural = "order_line"
        ordering = ['-id']
        db_table = "order_lines"

    def pre_save(self, list=[]):
        self.line_id = _get_unique_id(self, "LD", "line_id", list)

    def save(self, *args, **kwargs):
        self.pre_save()
        return super().save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.line_id)


def _get_unique_id(obj, code, field, list=[]):
    """
    :param _class:
    :return: unique_id
    """
    _class = obj.__class__
    _salt = helpers._gen_salt()
    _key = 0
    if _class.objects.filter().count():
        _key = _class.objects.latest('pk').pk
    if list:
        _key += len(list)
    _key += _salt
    unique_id = "{}{}".format(code, _key)
    try:
        for tries in range(1000):
            _class.objects.get(**{field: unique_id})
            _key += 1
        helpers.log('total tries: {}'.format(tries), level="info")
    except _class.DoesNotExist:
        pass
    return "{}{}".format(code, _key)
