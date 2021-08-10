from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from app.models import Question
from . import forms
from utils import helpers
from datetime import date, datetime


class AppView(ListView):
    model = Question

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        # handlers.authenticate(self.request)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        data_list = list(self.get_queryset().values())

        if 'page' in request.GET:
            page = request.GET.get('page')
            data_list = helpers.getPageData(page, data_list)

        data = {
            "size": len(data_list),
            "list": data_list
        }
        return JsonResponse(data, safe=False, status=200)

    def post(self, request):
        body = helpers.extractBody(request)
        data = []

        # Prepare Data
        for q in body:
            _form = forms.QuestionsForm(q)
            if(_form.is_valid()):
                form_data = _form.data
                parsed_date = helpers.parse_dt_str(form_data['pub_date'])
                data.append(Question(
                    question_text=form_data['question_text'],
                    pub_date=parsed_date
                ))
            else:
                helpers.log(_form.errors.as_json())
                return JsonResponse(_form.errors)

        Question.objects.bulk_create(data)

        return JsonResponse(data={
            'message': "Saved",
            "data": helpers.SelectFromObj(
                body,
                'question_text',
                'pub_date'
            )
        }, status=200)

    def delete(self, request):
        body = helpers.extractBody(request)

        Question. \
            objects. \
            all(). \
            delete() if (
                'all' in body
                and type(body['all']) == bool
                and body['all']
            ) else None

        Question. \
            objects. \
            filter(id__in=body['ids']). \
            delete() if (
                'ids' in body
                and type(body['ids']) == list
            ) else None

        return JsonResponse(data={'message': "Deleted", }, status=200)
