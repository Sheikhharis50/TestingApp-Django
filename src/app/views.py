from django.shortcuts import render
from api.app import views
from utils import requests


def index(request):

    res = requests.get('/api/questions', dict(page=1))
    context = dict(
        title="Home",
        data=res
    )
    return render(request, "questions/view_questions.html", context)
