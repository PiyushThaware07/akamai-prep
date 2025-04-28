from django.db import models
import datetime

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, default="Unknown Title")
    author = models.CharField(max_length=100, default="Unknown Author")
    published_date = models.DateField(default=datetime.date.today)
    
    def __str__(self):
        return self.title
