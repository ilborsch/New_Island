from django.db import models

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Articles(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    categories = models.ManyToManyField(Categories, blank=True)

