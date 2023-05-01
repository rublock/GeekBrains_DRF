from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    second_name = models.CharField(max_length=64)
    birthday_year = models.PositiveBigIntegerField()

    def __str__(self):
        return f'{self.first_name} {self.second_name}'


class Biography(models.Model):
    text = models.TextField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE, primary_key=True)



