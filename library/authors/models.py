from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=64)
    second_name = models.CharField(max_length=64)
    birthday_year = models.PositiveBigIntegerField()
    
