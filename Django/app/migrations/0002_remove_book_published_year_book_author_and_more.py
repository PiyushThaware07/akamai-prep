# Generated by Django 5.2 on 2025-04-28 11:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='published_year',
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default='Unknown Author', max_length=100),
        ),
        migrations.AddField(
            model_name='book',
            name='published_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default='Unknown Title', max_length=200),
        ),
    ]
