from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = "authors"

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    number_of_pages = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = "books"

    def __str__(self):
        return self.title
