# Generated by Django 5.0.4 on 2024-04-22 17:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_remove_book_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library.book'),
        ),
    ]
