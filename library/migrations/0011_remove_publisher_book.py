# Generated by Django 5.0.4 on 2024-04-22 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_auto_20240422_2051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publisher',
            name='book',
        ),
    ]