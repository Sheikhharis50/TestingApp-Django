from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from app.models import Question
from . import forms
from testing import helpers


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

        # Make Bulk Data
        for qs in body:
            _form = forms.QuestionsForm(qs)
            if(_form.is_valid()):
                form_data = _form.data
                parsed_date = helpers.parse_dt_str(form_data['pub_date'])
                data.append(Question(
                    question_text=form_data['question_text'],
                    pub_date=parsed_date
                ))
            else:
                return JsonResponse(_form.errors)

        # Insert Bulk Data
        Question.objects.bulk_create(data)

        return HttpResponse()
