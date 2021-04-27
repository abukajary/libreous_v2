from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import DetailView

from main.models import Employees, Books


def emp(request):
    return render(request, 'index.html', {'books_rating': Books.objects.all().order_by('-book_stars'),
                                          'books_date': Books.objects.all().order_by('book_date')})


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
