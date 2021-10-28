from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from app.models import Question
from . import forms
from utils import helpers
from . import serializers
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny


class AppView(APIView):
    model = Question
    permission_classes = [AllowAny]

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        # handlers.authenticate(self.request)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        data_list = list(Question.objects.all().values())
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
                return Response(_form.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

        Question.objects.bulk_create(data)

        return Response(data={
            'message': "Saved",
            "data": helpers.SelectFromObj(
                body,
                'question_text',
                'pub_date'
            )
        }, status=status.HTTP_200_OK)

    def delete(self, request):
        body = helpers.extractBody(request)

        queryset = Question.objects.all()

        if 'all' in body and int(body['all']):
            queryset.delete()
        elif 'id' in body:
            queryset.filter(id=body['id']).delete()

        return Response(data={'message': "Deleted", }, status=status.HTTP_200_OK)


class QuestionAPIView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = [AllowAny]

    def get(self, request):
        queryset = self.get_queryset().order_by('-id')
        serializer = serializers.QuestionSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(Question.objects.get(id=request.GET.get('id')))
        return super().post(request)
