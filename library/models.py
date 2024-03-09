from django.db import models

# Create your models here.
class Book(models.Model):
    book_title=models.CharField(max_length=500)
    book_authors= models.CharField(max_length=200)
    book_isbn=models.CharField(max_length=500,blank=True)
    book_isbn13=models.CharField(max_length=200,blank=True)
    book_pages=models.IntegerField(blank=True)
    book_publication_date=models.DateTimeField("date published",blank=True)
    book_publisher=models.CharField(max_length=200,blank=True)
    book_rating=models.FloatField(blank=True)
    book_total_ratings=models.IntegerField(blank=True)
    book_genres=models.CharField(max_length=500,blank=True)
    book_description=models.CharField(max_length=500,blank=True)
    book_file=models.FileField(upload_to="uploads/",default="NULL")
    def __str__(self):
        return self.book_title