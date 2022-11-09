from django.shortcuts import render
from rest_framework import generics
from .models import Articles
from .serializers import ArticleSerializer


# Create your views here.


class ArticlesAPIView(generics.ListAPIView):
    queryset = Articles.objects.all()
    serializer_class = ArticleSerializer
