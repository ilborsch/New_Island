from rest_framework import serializers
from rest_framework.response import Response

from .models import Articles, Categories


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'

#    title = serializers.CharField(max_length=150)
#    description = serializers.CharField(max_length=1000)
#    date_created = serializers.DateTimeField(allow_null=True, read_only=True)
#    is_published = serializers.BooleanField(default=True, allow_null=True)
#    categories = CategoriesSerializer(read_only=True, many=True)

#    def create(self, **valid_data):
#        return ArticleSerializer.objects.create(**valid_data)

#    def update(self, instance, validated_data):
#        instance.title = validated_data.get('title', instance.title)
#        instance.description = validated_data.get('description', instance.description)
#        instance.date_created = validated_data.get('date_created', instance.date_created)
#        instance.is_published = validated_data.get('is_published', instance.is_published)
#        instance.categories = validated_data.get('categories', instance.categories)
#
#    def delete(self, request, *args, **kwargs):
#        pk = kwargs.get('pk', None)
#        if not pk:
#            return Response({"post": "Delete post " + str(pk)})
#
#        return Response({"post": "Delete post " + str(pk)})