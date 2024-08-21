from django.db import models
from django.urls import reverse

# Create your models here.
class Author(models.Model):
    title = models.TextField()
    publish_date= models.DateField()

    def get_absolute_url(self):
        return reverse('author_detail',kwargs={'pk': self.pk})
    
    def __str__(self):
        return self.title[0:20]

class Publisher(models.Model):
    title = models.TextField()
    description = models.TextField()
    books=models.ManyToManyField('Book', related_name='books')

    def get_absolute_url(self):
        return reverse('publisher_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title[0:20]
    

class Book(models.Model):
    title = models.TextField()
    publish_date= models.DateField()
    authors= models.ManyToManyField('Author', related_name='books')

   
    def get_absolute_url(self):
        return reverse('book_detail',kwargs={'pk': self.pk})
    
    def __str__(self): 
        return self.title[0:20]

