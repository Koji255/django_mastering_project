from django.utils import timezone

from django.db import models
from django.db.models import Q
from django.core.validators import MinLengthValidator

# Create your models here.
class User(models.Model):
    surname = models.CharField(max_length=50, default=None)
    lastname = models.CharField(max_length=50, default=None)
    nickname = models.CharField(max_length=50, default=None)
    email = models.EmailField(default=None)
    password = models.CharField(validators=[MinLengthValidator(8)], max_length=24, default=None)
    account_creation_date = models.DateTimeField(default=timezone.now())

    class Meta:
        db_table = "users"
        ordering = ["account_creation_date"]

    def __str__(self):
        return self.nickname