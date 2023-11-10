from django.contrib import admin
from book_shop.models import *
# Register your models here.

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Author)
