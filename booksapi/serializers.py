from rest_framework import serializers

from .models import *


class CategorySlz(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BookSlz(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BookSourceSlz(serializers.ModelSerializer):
    class Meta:
        model = BookSource
        fields = "__all__"


class BookReviewSlz(serializers.ModelSerializer):
    class Meta:
        model = BookReview
        fields = ['book', 'name', 'job', 'retext']


class CommentSlz(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['book','name','text','created']