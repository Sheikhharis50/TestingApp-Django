from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from app_orders import models
from . import forms
from utils import helpers


class AppOrdersView(APIView):
    model = models.Orders
    permission_classes = [AllowAny]

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        # handlers.authenticate(self.request)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        data_list = list(self.model.objects.all().values())
        data = {}

        if 'page' in request.GET:
            page = request.GET.get('page')
            size = request.GET.get('size')
            data_list, has_next = helpers.getPageData(page, size, data_list)
            data['page'] = page
            data['size'] = size
            data['has_next'] = has_next

        data.update({"list": data_list})
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        body = request.data

        # create Order
        order_form = forms.OrdersForm(body)
        order = None
        if order_form.is_valid():
            order = order_form.save()
        else:
            return Response(order_form.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        if 'bulk' in body and int(body['bulk']):
            # Bulk insertion
            data = []
            for q in body['line_items']:
                q['order'] = order.id
                order_line_form = forms.OrderLineForm(q)
                if(order_line_form.is_valid()):
                    line_item = models.Order_line(**order_line_form.cleaned_data)
                    models.Order_line.pre_save(line_item, data)
                    data.append(line_item)
                else:
                    helpers.log(order_line_form.errors.as_json())
                    return Response(order_line_form.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

            models.Order_line.objects.bulk_create(data)
        else:
            # Individual insertion
            pass

        return Response(data={
            'message': "Saved",
            # "data": helpers.SelectFromObj(
            #     body,
            #     'question_text',
            #     'pub_date'
            # )
        }, status=status.HTTP_200_OK)
