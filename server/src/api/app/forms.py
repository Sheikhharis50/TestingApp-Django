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
        required=False
    )

    def isQuestionExist(self, q_text):
        data_list = self.data['data_list']

        def exists(q):
            return q.question_text == q_text

        return True if len(list(filter(exists, data_list))) >= 1 else False

    def clean_question_text(self):
        q_text = self.cleaned_data['question_text']
        if 'ignore_validation' in self.data and self.data['ignore_validation']:
            return q_text

        # Validations
        if Question.objects.filter(question_text=q_text).exists():
            raise exceptions.ValidationError(
                'Question text `{}` already exists'.format(q_text)
            )
        if 'data_list' in self.data and self.isQuestionExist(q_text):
            raise exceptions.ValidationError(
                'Question text `{}` duplications'.format(q_text)
            )

        return q_text
