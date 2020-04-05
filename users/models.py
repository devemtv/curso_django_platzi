
# Django
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """Profile model

    Proxy model that extends the base data with other
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(blank=True, max_length=200)
    biography = models.TextField(blank=True)
    phone_number = models.CharField(max_length=20)

    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True,
    )

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username"""
        return self.user.username
