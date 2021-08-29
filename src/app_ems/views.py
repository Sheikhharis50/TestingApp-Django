from django.http.response import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import render_to_string
from django.views import View
from app_ems.models import Author, Book
from .forms import BookFormset, BookModelFormset, AuthorForm
from django.http import JsonResponse
from utils.helpers import log


class AuthorView(View):
    model = Author
    queryset = model.objects.all()
    template_name = "authors/authors_list.html"

    def get(self, request):
        authors = self.model.objects.all()
        context = dict(
            title="Authors List",
            keys=["name"],
            link_fields=["name"],
            authors=authors,
        )
        return render(request, self.template_name, context)


class AuthorDetailView(View):
    form_class = AuthorForm
    model = Author
    queryset = model.objects.all()
    template_name = "authors/author_detail.html"
    title = "Authors Detail"

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get(self, request, pk):
        author = self.get_object(pk)
        form = self.form_class(instance=author)

        bv = BookView()
        res = bv.get(request, pk)

        context = {
            'title': self.title,
            'form': form,
            'books_html': res.content.decode("utf-8")
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        author = self.get_object(pk)
        form = self.form_class(request.POST or None, instance=author)
        if form.is_valid():
            form.save()
            return redirect('authors_view')

        context = {
            'title': self.title,
            'form': form,
        }
        return render(request, self.template_name, context)

    def delete(self, request, pk):
        try:
            author = self.get_object(pk)
            author.delete()
            data = {'message': 'Deleted!'}
            return JsonResponse(data, status=200)
        except Exception as e:
            log(e)
        return Http404


class BookView(View):
    model = Book
    queryset = model.objects.all()
    template_name = "books/books_list.html"

    def get(self, request, pk):
        books = self.model.objects.filter(author__id=pk)
        context = dict(
            keys=["title", "number_of_pages"],
            link_fields=["title"],
            books=books,
        )
        return render(request, self.template_name, context)


class BookView(View):
    model = Book
    queryset = model.objects.all()
    template_name = "books/add_book.html"
    title = "Add Book"

    def getAuthur(self, pk):
        return Author.objects.get(pk=pk)

    def get(self, request, pk):
        author = self.getAuthur(pk)
        formset = BookModelFormset(
            queryset=self.queryset.filter(author__id=pk)
        )
        context = dict(
            formset=formset,
            title=self.title,
            author=author
        )
        return render(request, self.template_name, context)

    def post(self, request, pk):
        author = self.getAuthur(pk)
        formset = BookModelFormset(request.POST or None)
        if formset.is_valid():
            formset.instance = author
            formset.save()
            return redirect('authors_detail_view', pk=author.id)
        context = dict(
            formset=formset,
            title=self.title,
            author=author
        )
        return render(request, self.template_name, context)


def add_book_form(request):
    formset = BookFormset()
    context = dict(
        formset=formset
    )
    html = render_to_string('books/partials/book_form.html', context)
    return HttpResponse(html)
