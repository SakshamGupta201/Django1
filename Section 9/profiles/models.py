from django.db import models

# Create your models here.


class UserProfile(models.Model):
    """Model definition for UserProfile."""

    class Meta:
        """Meta definition for UserProfile."""

        verbose_name = "UserProfile"
        verbose_name_plural = "UserProfiles"

    image = models.ImageField(upload_to="images")
