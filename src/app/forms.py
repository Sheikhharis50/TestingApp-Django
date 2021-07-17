from django import forms
from django.forms import Form
from django.core import exceptions
from app.models import Question


class QuestionsForm(Form):
    question_text = forms.CharField(
        label='Question Text',
        max_length=200,
        required=True,
    )
    pub_date = forms.DateTimeField(
        label='Publish Date',
        input_formats=['%d-%m-%Y'],
        required=True
    )

    def clean_question_text(self):
        data = self.cleaned_data['question_text']
        if Question.objects.filter(question_text=data).exists():
            raise exceptions.ValidationError(
                'Question text `{}` already exists'.format(data)
            )
        return data
