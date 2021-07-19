from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from app.models import Question
from . import forms
from testing import helpers
import datetime


def index(request):
    return HttpResponse("Hi, it's a Testing APP")


class AppView(ListView):
    model = Question

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        # handlers.authenticate(self.request)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return JsonResponse(list(self.get_queryset().values()), safe=False)

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
                return JsonResponse(_form.errors)

        # Bulk Creation
        # ==============================>
        t1 = datetime.datetime.now()
        # Prepare Bulk Data

        # Insert Bulk Data
        Question.objects.bulk_create(data)

        # Measuring Time
        t2 = datetime.datetime.now()
        print('\nBulk Creation Took: {}'.format(t2-t1))
        # ==============================>

        # Individual Creation
        # ==============================>
        t1 = datetime.datetime.now()

        # Insert Individual Data
        for q in data:
            q.save()

        # Measuring Time
        t2 = datetime.datetime.now()
        print('Individual Creation Took: {}\n'.format(t2-t1))
        # ==============================>

        return JsonResponse(data={
            'message': "Saved",
            "data": helpers.SelectFromObj(
                body,
                'question_text',
                'pub_date'
            )
        })

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

        return JsonResponse(data={'message': "Deleted", })
