# Generated by Django 5.0.4 on 2024-04-22 16:00

from django.db import migrations


class Migration(migrations.Migration):

    def make_many_authors(apps, schema_editor):


        Book = apps.get_model('library','Book')

        for book in Book.objects.all():
            book.authors.add(book.author)

    dependencies = [
        ('library', '0003_book_authors_alter_book_author'),
    ]

    operations = [ migrations.RunPython(make_many_authors)
    ]
