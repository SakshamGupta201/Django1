from datetime import date
from django.shortcuts import get_object_or_404, render
from blog.models import Post

# Create your views here.


def index(request):
    all_posts = Post.objects.all().order_by("date")[:3]

    return render(request, "blog/blog.html", {"posts": all_posts})


def posts(request):
    posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {"posts": posts})


def detail_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {"post": post, 'tags': post.tag.all()})
