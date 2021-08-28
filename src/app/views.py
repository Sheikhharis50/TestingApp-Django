from django.shortcuts import render
from utils import requests


def index_view(request):
    return render(request, "base.html")


def about_view(request):
    return render(request, "pages/about.html")


def questions_list_view(request):
    res = requests.get(request, 'questions', dict(page=0, size=5))
    context = dict(
        title="Home",
        data=res
    )
    return render(request, "questions/view_questions.html", context)
