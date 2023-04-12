from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.HomeView.as_view(), name='homepage'),
    path('books/', views.BooksListView.as_view(), name="books_list"),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name="book_detail")
]