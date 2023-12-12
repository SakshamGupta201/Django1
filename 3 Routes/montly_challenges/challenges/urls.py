from django.urls import path
from . import views

urlpatterns = [
    path("", views.challenges, name="challenges"),
    path("<int:month>/", views.month_challenge_by_number),
    path("<str:month>/", views.index, name="month_challenge"),
]
