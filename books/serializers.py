from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from books.models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        if not title.isalpha():
            raise ValidationError(
                {
                    "status": False,
                    "message": "Title should only contain letters"
                }
            )

        if Book.objects.filter(title=title, author=author):
            raise ValidationError(
                {
                    "status": False,
                    "message": "Title already exists"
                }
            )
        return data


    def validate_price(self, price):
        if price <= 0 or price >= 9999999999:
            raise ValidationError(
                {
                    "status": False,
                    "message": "Price should be between 0 and 9999999999 "
                }
            )