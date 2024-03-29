from django.db import models

# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=25, unique=True)
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.username