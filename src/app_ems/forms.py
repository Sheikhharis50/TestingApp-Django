from django import forms
from django.forms import widgets
from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory, modelformset_factory
from . import models


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = (
            "title", "number_of_pages"
        )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'number_of_pages': forms.NumberInput(attrs={'class': 'form-control'}),
        }


BookModelFormset = modelformset_factory(
    model=models.Book,
    form=BookForm,
    extra=0
)

BookFormset = formset_factory(
    form=BookForm,
    extra=0
)


class AuthorForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = (
            "name",
        )
