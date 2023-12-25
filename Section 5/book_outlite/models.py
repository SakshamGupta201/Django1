from collections.abc import Iterable
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    author = models.CharField(max_length=100, default="")
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="")

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Title: {self.title} | Rating: {self.rating} | Author: {self.author} | Bestselling: {self.is_bestselling}"
