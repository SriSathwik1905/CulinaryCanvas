from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture_url = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.username