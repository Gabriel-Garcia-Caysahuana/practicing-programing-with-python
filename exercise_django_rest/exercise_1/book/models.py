from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20) 
    published_date = models.DateField()
    isb = models.IntegerField()

    def __str__(self):
        return self.title