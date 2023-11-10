from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, DetailView, ListView, CreateView

from book_shop.models import *
from book_shop.forms import *

# Create your views here.


class Home(ListView):
    template_name = 'index.html'
    model = Book
    context_object_name = 'books'



class CatalogView(TemplateView):
    template_name = 'catalog.html'


class RegistrationView(TemplateView):
    template_name = 'Registration.html'


class DetailBookView(DetailView):
    template_name = 'detail_book.html'
    model = Book
    context_object_name = 'book'
    pk_url_kwarg = 'id'


class CreateBookView(CreateView):
    template_name = 'create_book.html'
    form_class = FormBook
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Author.objects.all()
        context['genres'] = Genre.objects.all()
        context['languages'] = Language.objects.all()
        return context

    def form_invalid(self, form):
        print(form.errors)
        return render(self.request, 'create_book.html', {'form': form})

    def get_success_url(self):
        return reverse('home')


class CreateAuthorView(CreateView):
    template_name = 'create_author.html'
    form_class = FormAuthor
    model = Author

    def get_success_url(self):
        return reverse('home')


class CreateGenreView(CreateView):
    template_name = 'create_author.html'
    form_class = FormGenre
    model = Genre

    def get_success_url(self):
        return reverse('home')