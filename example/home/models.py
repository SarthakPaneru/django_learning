from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    desc = models.TextField()
    author = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.name