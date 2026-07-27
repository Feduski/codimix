from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    credits = models.IntegerField(default=5)

    def __str__(self):
        return self.username