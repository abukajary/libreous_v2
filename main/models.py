from django.db import models

# Create your models here.
from django.urls import reverse


class Employees(models.Model):
    id = models.FloatField(primary_key=True)
    emp_name = models.CharField(max_length=50, blank=True, null=True)
    emp_email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class BookAuthors(models.Model):
    id = models.FloatField(primary_key=True)
    author_name = models.CharField(max_length=50, blank=True, null=True)
    author_surname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_authors'

    def __str__(self):
        full_name = str(self.author_name) + " " + str(self.author_surname)
        return full_name


class Books(models.Model):
    id = models.BigIntegerField(primary_key=True)
    book_img = models.CharField(max_length=500, blank=True, null=True)
    book_name = models.CharField(max_length=50)
    book_author = models.ForeignKey(BookAuthors, models.DO_NOTHING, db_column='book_author')
    book_date = models.DateField(blank=True, null=True)
    book_stars = models.IntegerField(blank=True, null=True)
    book_price = models.BigIntegerField(blank=True, null=True)
    book_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books'

    def __str__(self):
        return self.book_name

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})