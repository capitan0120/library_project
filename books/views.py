from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from books.models import Book
from books.serializers import BookSerializer


# class BookListAPIView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookListAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True).data
        data = {
            "status": "success",
            "data": serializer
        }
        return Response(data)


# class BookDetailAPIView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookDetailAPIView(APIView):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        data = serializer.data
        return Response(data)
        # try:
        #     book = Book.objects.get(pk=pk)
        #     serializer = BookSerializer(book)
        #     data = {
        #         "status": "success",
        #         "data": serializer.data
        #     }
        #     return Response(data)
        # except Book.DoesNotExist:
        #     return Response("Book not found", status=status.HTTP_404_NOT_FOUND)


# class BookUpdateAPIView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookUpdateAPIView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(data=request.data, instance=book, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = serializer.data
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BookDeleteAPIView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookDeleteAPIView(APIView):
    def delete(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        # try:
        #     book = Book.objects.get(pk=pk)
        #     book.delete()
        #     return Response("Book delete successfully", status=status.HTTP_204_NO_CONTENT)
        # except Book.DoesNotExist:
        #     return Response("Not Found Book", status=status.HTTP_404_NOT_FOUND)


# class BookCreateAPIView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


class BookCreateAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status": "success",
                "data": serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
