from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom User model."""

    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='email',
    )
    second_name = models.CharField(max_length=200, verbose_name='Second_name')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['username']
