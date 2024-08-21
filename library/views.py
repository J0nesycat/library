from django.shortcuts import render
from accounts import models


#from django.http import HttpResponse
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Book,Author,Publisher
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
class BookDeleteView(LoginRequiredMixin,DeleteView):
     model = Book
     success_url ="/"
     template_name = "confirm_delete.html"
     
     def dispatch(self, request, *args, **kwargs):
        # Check if the user is allowed to delete the book
        if not self.request.user.is_superuser:  # For example, only superuser can delete books
            # You can also check for other conditions like book ownership or specific permissions
            return self.handle_no_permission()
        
        return super().dispatch(request, *args, **kwargs)

class PublisherUpdateView(LoginRequiredMixin,UpdateView):
     model= Publisher
     template_name = "publisher_edit.html"
     fields = ["title", "description","books"]


class PublisherCreateView(LoginRequiredMixin,CreateView):
     model = Publisher
     template_name = "publisher_new.html"
     fields = ["title", "description","books"]


class PublishersDetailView(DetailView):
     model=Publisher
     template_name="publisher_detail.html"

 
class PublisherPageView(ListView):
     model=Publisher
     template_name= "publishers.html" 

class AuthorUpdateView(LoginRequiredMixin,UpdateView):
    model= Author
    template_name = "author_edit.html"
    fields = ["title", "publish_date"]

class AuthorCreateView(LoginRequiredMixin,CreateView):
    model = Author
    template_name = "author_new.html"
    fields = ["title", "publish_date"]

   
class AuthorsDetailView(DetailView):
     model=Author
     template_name="author_detail.html"

class AuthorPageView(ListView):
    model=Author
    template_name= "authors.html"

class BookUpdateView(LoginRequiredMixin,UpdateView):
    model= Book
    template_name = "book_edit.html"
    fields = ["title", "publish_date","authors"]

class BookCreateView(LoginRequiredMixin,CreateView):
    model = Book
    template_name = "book_new.html"
    fields = ["title", "publish_date","authors"]


class BooksDetailView(DetailView):
     model=Book
     template_name="book_detail.html"

class BooksPageView(ListView):
    model=Book
    template_name= "books.html"

class AboutPage(TemplateView):

    template_name="about.html"

class HomePageView(TemplateView):

    template_name="home.html"












