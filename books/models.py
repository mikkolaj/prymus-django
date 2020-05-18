from django.db import models


# Create your models here.
class Book(models.Model):
    # id (django z góry definiuje pole id, jest unikatowe)
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    published = models.DateTimeField()
    author = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.title
