from django.urls import path
from book_shop.views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('book/<int:id>/', DetailBookView.as_view(), name='book-detail'),
    path('create/', CreateBookView.as_view(), name='create-book'),
    path('create/author', CreateAuthorView.as_view(), name='create-author'),
    path('create/genre', CreateGenreView.as_view(), name='create-genre'),
]