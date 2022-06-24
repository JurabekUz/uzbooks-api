from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Category, Book, Comment
from .serializers import CategorySlz, BookSlz, CommentSlz, BookSourceSlz, BookReviewSlz

# Category View
class CategoryList(APIView):
    def get(self, request):
        # Categoriyalarni olamiz (object)
        categories = Category.objects.all()
        #object serializerga uzatiladi. serializerdan dict qaytadi
        serializer = CategorySlz(categories,many=True)
        #json farmat qaytaramiz
        return Response(data=serializer.data)

''' CategoryBooksList va CategoryBooks ikkalasi bir xil View har xil shaklda yozilgan '''
# category modeli orqali unga tegishli booklarni olamiz
class CategoryBooks(APIView):
    def get(self, request, pk):
        # Ayni categoriyani tanlab olamiz
        category = Category.objects.get(pk=pk)

        # Ayni kategoriyaga tegishli kitoblarni olamiz
        books = category.book.all() # book bu yerda ralated_name
        #books = Category.objects.filter(category__id=pk)

        serializer = BookSlz(books, many=True)
        return Response(data=serializer.data)

class BooksList(APIView):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'author']
    search_fields = ['title', 'author', 'snippet']

    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        # books objectni serializer laymiz
        serializer = BookSlz(books, many=True)
        # json data qaytaramiz
        return Response(data=serializer.data)


class BookDetail(APIView):
    def get(self, request, pk):
        # book ni id orqali olamiz
        book = Book.objects.get(pk=pk)
        source = book.source.all()
        review = book.review.all()

        # book objectni serializer laymiz
        bookslz = BookSlz(book)

        # source larni serializer laymiz
        sourceslz = BookSourceSlz(source, many=True)

        # review larni serializer laymiz
        reviewslz = BookReviewSlz(review, many=True)

        # json data qaytaramiz
        return Response( data={
            'book': bookslz.data,
            'source' : sourceslz.data,
            'review' : reviewslz.data
        })

"""
# category ning id si orqali unga tegishli booklarni olamiz
class CategoryBooksList(APIView):
    def get(self, request, pk):
        # pk bu yerda category id si
        category_books = Book.objects.filter(category__id=pk)
        # category_books objectni serializer laymiz
        serializer = BookSlz(category_books, many=True)
        # json data qaytaramiz
        return Response(data=serializer.data)
"""

# Kitob ga tegishli Commentslarni korish va qo'shish
class CommentView(APIView):
    # Izohlarni ko'rish
    def get(self, request, pk):
        #pk bu kitob ID si hisoblandi
        book = Book.objects.get(pk=pk)
        # book objectni ning related_name ni orqali unga tegishli barcha commentlarni olamiz
        comments = book.comment.all()
        # izohlarni serializere laymiz
        serializer = CommentSlz(comments, many=True)
        # json data qaytaramiz
        return Response(data=serializer.data)

    #izoh qo'shish
    #post funksiyaga pk ni foydalanmasak ham qo'shishimiz kerak chunki urlda pk ni ishlatganmiz
    def post(self, request, pk):
        serializer = CommentSlz(data=request.data)
        # serializer valid ligini tekshiramiz
        if serializer.is_valid(raise_exception=True):
            comment = serializer.save()
        return redirect('comment_view', pk)

'''
class BookSearch(APIView):
    def get(self, request):
        query = request.data.get('search')
        from django.db.models import Q
        books = Book.objects.filter(
            Q(title__contains = query) |
            Q(author__contains = query) |
            Q(snippet__contains = query)
        )
        serializer = BookSlz(books, many=True)
        return Response(data=serializer.data)

'''







