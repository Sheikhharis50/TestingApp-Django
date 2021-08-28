from django.shortcuts import render
from utils import requests


def index(request):
    res = requests.get(request, 'questions', dict(page=0, size=5))
    context = dict(
        title="Home",
        data=res
    )
    return render(request, "questions/view_questions.html", context)


def questions(request):
    print(request.get_full_path())
    return render(request, "questions/questions_list.html", {})
