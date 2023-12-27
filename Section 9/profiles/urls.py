from django.urls import path

from . import views

urlpatterns = [
    path("", views.CreateProfileView.as_view(), name="profiles"),
    path("list", views.ProfileListView.as_view()),
]
