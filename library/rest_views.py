from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Book, Author, Publisher
from .serializers import BookSerializer,AuthorSerializer,PublisherSerializer


class BookListAPIView(APIView):
    def get(self,request):
        list_of_books = Book.objects.all()
        serializer= BookSerializer(list_of_books, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        data= {
            'title': request.data.get('title'),
            'publish_date': request.data.get('publish_date'),
            'authors':request.data.get('authors')
        }
        book = BookSerializer(data=data)
        if book.is_valid():
            book.save()
            return Response(book.data, status=status.HTTP_201_CREATED)
        
        return Response(book.errors, status=status.HTTP_400_BAD_REQUEST)
    

class AuthorListAPIView(APIView):
    def get(self,request):
        list_of_authors = Author.objects.all()
        serializer= AuthorSerializer(list_of_authors, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        data= {
            'title': request.data.get('title'),
            'publish_date': request.data.get('publish_date')
            
        }
        author = AuthorSerializer(data=data)
        if author.is_valid():
            author.save()
            return Response(author.data, status=status.HTTP_201_CREATED)
        
        return Response(author.errors, status=status.HTTP_400_BAD_REQUEST)


class PublisherListAPIView(APIView):
    def get(self,request):
        list_of_publishers = Publisher.objects.all()
        serializer = PublisherSerializer(list_of_publishers, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        data= {
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'books': request.data.get('books'),
            
        }
        publisher = PublisherSerializer(data=data)
        if publisher.is_valid():
            publisher.save()
            return Response(publisher.data, status=status.HTTP_201_CREATED)
        
        return Response(publisher.errors, status=status.HTTP_400_BAD_REQUEST)