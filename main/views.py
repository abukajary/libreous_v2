

from django.db.models import Count, Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.template import Context, loader
from django.views.generic import DetailView

from main.models import Employees, Books


def emp(request):
    top_rated_books = Books.objects.all().order_by('-book_stars')
    latest_date_published_books = Books.objects.all().order_by('book_date')

    return render(request, 'index.html', {'rating': top_rated_books, 'date': latest_date_published_books})


def go_search(request):
    query = request.GET.get('q')
    return render(request, 'search.html', {'books': Books.objects.filter(
        Q(book_name__icontains=query) | Q(book_author__author_name__icontains=query) |
        Q(book_author__author_surname__icontains=query)
    ), 'q': query})


def book_detail(request, pk):
    alo = Books.objects.filter(
        Q(id__exact=pk)
    )
    return render(request, 'detail/book_detail.html', {'book': alo})
