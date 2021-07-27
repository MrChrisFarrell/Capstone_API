from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    """Our custom user model that adds a new field to the default django user model"""
    is_owner = models.BooleanField(default=False)

    def __str__(self):
        return self.username
