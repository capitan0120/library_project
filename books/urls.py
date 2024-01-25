from django.urls import path

from books.views import(
    BookListAPIView, BookDetailAPIView,
    BookUpdateAPIView, BookDeleteAPIView, BookCreateAPIView,
    BookListCreateAPIView, BookRetrieveUpdateDeleteAPIView
)

urlpatterns = [
    path('books/', BookListAPIView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', BookUpdateAPIView.as_view()),
    path('books/<int:pk>/delete/', BookDeleteAPIView.as_view()),
    path('books/create/', BookCreateAPIView.as_view(), name='book-create'),

    path('book/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('book/<int:pk>/', BookRetrieveUpdateDeleteAPIView.as_view(), name='book')

]