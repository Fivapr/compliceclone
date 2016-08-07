from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Goal(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=100)
    importance = models.CharField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)



    def __str__(self):
        return self.name