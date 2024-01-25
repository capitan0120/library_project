from django.db.models import Model, CharField, DecimalField, TextField


class Book(Model):
    title = CharField(max_length=250)
    subtitle = CharField(max_length=250)
    content = TextField()
    author = CharField(max_length=250)
    isbn = CharField(max_length=13)
    price = DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.title
