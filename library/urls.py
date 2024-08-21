from django.urls import path
# from .views import library_home_page
from .views import HomePageView, AboutPage
from .views import AuthorCreateView, AuthorUpdateView, AuthorsDetailView, AuthorPageView
from .views import BookUpdateView,BookCreateView, BooksDetailView, BooksPageView
from .views import PublisherUpdateView,PublisherCreateView,PublishersDetailView,PublisherPageView
from .views import BookDeleteView

from .rest_views import BookListAPIView,AuthorListAPIView,PublisherListAPIView

urlpatterns = [
    path('book/<int:pk>/delete/', BookDeleteView.as_view(),name="confirm_delete"),
    path("", HomePageView.as_view(),name="home"),
    path("about/", AboutPage.as_view(), name='about'), 
    path("books/", BooksPageView.as_view(), name='books'),  
    path("book/<int:pk>", BooksDetailView.as_view(), name="book_detail"),
    path("book/new/", BookCreateView.as_view(), name="book_new"),
    path("book/<int:pk>/edit/", BookUpdateView.as_view(), name="book_edit"),
    path("author/", AuthorPageView.as_view(), name="author"),
    path("author/<int:pk>", AuthorsDetailView.as_view(), name="author_detail"),
    path("author/new/", AuthorCreateView.as_view(), name="author_new"),
    path("author/<int:pk>/edit/", AuthorUpdateView.as_view(), name="author_edit"),
    path("publishers/", PublisherPageView.as_view(), name="publishers"),  
    path("publisher/<int:pk>", PublishersDetailView.as_view(), name="publisher_detail"),
    path("publisher/new/", PublisherCreateView.as_view(), name="publisher_new"),
    path("publisher/<int:pk>/edit/", PublisherUpdateView.as_view(), name="publisher_edit"),

    path("api/books/", BookListAPIView.as_view(http_method_names=['get'])),
    path("api/book/", BookListAPIView.as_view(http_method_names=['post'])),
    path("api/authors/", AuthorListAPIView.as_view(http_method_names=['get'])),
    path("api/author/", AuthorListAPIView.as_view(http_method_names=['post'])),
    path("api/publishers/", PublisherListAPIView.as_view(http_method_names=['get'])),
    path("api/publisher/", PublisherListAPIView.as_view(http_method_names=['post'])),
]