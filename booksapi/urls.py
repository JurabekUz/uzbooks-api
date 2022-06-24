from django.urls import path
from .views import CategoryList, BooksList, BookDetail,CategoryBooks,CommentView

urlpatterns = [
    path('categories/',CategoryList.as_view()),
    path('categories/<int:pk>/', CategoryBooks.as_view()),
    path('books/', BooksList.as_view()),
    path('books/<int:pk>/', BookDetail.as_view()),
    path('books/<int:pk>/comment', CommentView.as_view(), name='comment_view'),
]