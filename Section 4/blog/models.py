from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.


class Tag(models.Model):
    # Model for representing tags
    caption = models.CharField(max_length=50)

    def __str__(self):
        # String representation of a tag
        return self.caption


class Author(models.Model):
    # Model for representing authors
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        # String representation of an author
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    # Model for representing blog posts
    title = models.CharField(max_length=50)
    # image_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="posts",null=True)
    excerpt = models.CharField(max_length=150)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(blank=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts"
    )
    tag = models.ManyToManyField(Tag, related_name="posts")

    def __str__(self):
        # String representation of a blog post
        return self.title
