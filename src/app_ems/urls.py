from django.urls import path
from . import views

urlpatterns = [
    path('', views.AuthorView.as_view(), name='authors_view'),
    # path('author/<pk>',
    #      views.AuthorDetailView.as_view(),
    #      name='authors_detail_view'
    #      ),
    path('author/<int:pk>',
         views.BookView.as_view(),
         name='authors_detail_view'
         ),
    path('author/book-form', views.add_book_form, name='book_form')
]
