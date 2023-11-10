from django import forms
from book_shop.models import *

class FormBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'image', 'article', 'genres', 'publication_date', 'price', 'is_available', 'language']


class FormAuthor(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']


class FormGenre(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']