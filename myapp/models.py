from django.utils import timezone

from django.db import models
from django.db.models import Q

# Create your models here.
class User(models.Model):
    surname = models.CharField(max_length=50, default="")
    lastname = models.CharField(max_length=50, default="")
    nickname = models.CharField(max_length=50, default="")
    email = models.EmailField(default=None)
    password = models.CharField(max_length=20, default="")
    account_creation_date = models.DateTimeField(default=timezone.now())

    class Meta:
        db_table = "users"
        ordering = ["account_creation_date"]

    def __str__(self):
        return self.nickname