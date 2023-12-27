from django.urls import path

from reviews import views

urlpatterns = [
    path("", views.ReviewView.as_view(), name="review"),
    path("thank_you/", views.ThankYouView.as_view(), name="thank_you"),
    path("reviews/", views.ReviewListView.as_view(), name="reviews"),
    path("reviews/favourite/", views.AddFavoriteView.as_view()),
    path("reviews/<int:pk>", views.ReviewDetailView.as_view(), name="single_review"),
]
