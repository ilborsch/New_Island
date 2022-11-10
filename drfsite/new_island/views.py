from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Articles
from .serializers import ArticleSerializer


# Create your views here.


class ArticleAPIList(generics.ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Articles.objects.all()


class ArticleAPIUpdate(generics.UpdateAPIView):
    serializer_class = ArticleSerializer
    queryset = Articles.objects.all()


class ArticleAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Articles.objects.all()


class ArticlesAPIView(APIView):

    def get(self, request):
        articles = Articles.objects.all()
        return Response({'posts': ArticleSerializer(articles, many=True).data})

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'post': serializer.data})
