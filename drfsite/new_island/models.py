from django.db import models

# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=30)



class Articles(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    categories = models.ManyToManyField(Categories, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title

