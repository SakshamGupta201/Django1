from django.http import Http404
from django.shortcuts import get_object_or_404, render
from book_outlite.models import Book
from django.db.models import Avg, Min

# Create your views here.


def index(request):
    books = Book.objects.all().order_by("title",'rating')
    num_books = books.count()
    average_rating = books.aggregate(Avg("rating"), Min("rating"))
    print(average_rating)
    return render(
        request,
        "book_outlet/index.html",
        {
            "books": books,
            "total_number_of_books": num_books,
            "average_rating": round(average_rating.get("rating__avg")),
        },
    )


def book_detail(request, slug):
    book = get_object_or_404(Book.objects.filter(slug=slug))

    return render(
        request,
        "book_outlet/book_detail.html",
        {
            "title": book.title,
            "auhor": book.author,
            "is_bestseller": book.is_bestselling,
        },
    )
