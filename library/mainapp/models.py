from django.db import models

from authors.models import Author


class Book(models.Model):
    name = models.CharField(max_length=32)
    authors = models.ManyToManyField(Author)


class Article(models.Model):
    name = models.CharField(max_length=32)
    text = models.TextField()
    author = models.ForeignKey(Author, models.PROTECT)

# class Author(models.Model):
#     name = models.CharField(max_length=32)
#     birthday_year = models.PositiveIntegerField()

#     def __str__(self):
#         return self.name


# class Biography(models.Model):
#     text = models.TextField()
#     author = models.OneToOneField(Author, on_delete=models.CASCADE)
