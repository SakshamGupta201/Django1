from django.urls import path

from blog import views


urlpatterns = [
    path("", views.index, name="home"),
    path("posts", views.posts, name="posts_page"),
    path("posts/<slug:slug>", views.detail_post, name="detail_post_page")
]
