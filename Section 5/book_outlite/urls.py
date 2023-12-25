from django.urls import path
from book_outlite.views import index, book_detail

urlpatterns = [
    path("", view=index, name="index"),
    path("<slug:slug>", view=book_detail, name="book_detail"),
]
