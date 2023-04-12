from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from books.models import Book


class BaseView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        return context
    

class BooksListView(ListView):
    queryset = Book.objects.order_by("-id")
    template_name = "books/books.html"
    context_object_name = "books"


@method_decorator(csrf_exempt, name='dispatch')
class HomeView(BooksListView):

    method_decorator
    def post(self, req, **kwargs):
        print(req.POST)

        return super().get(req, **kwargs)


class BookDetailView(DetailView):
    queryset = Book.objects.all()
    template_name = "books/book_detail.html"
    context_object_name = "book"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     book_id = self.kwargs.get(self.pk_url_kwarg)
    #     context["first_book"] = Book.objects.first()
    #     context["book"] = Book.objects.filter(id=book_id).first()
    #     return context