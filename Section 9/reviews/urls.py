from django.urls import path

from reviews import views

urlpatterns = [
    path("", views.review, name="review"),
    path("thank_you", views.thank_you, name="thank_you"),
]
