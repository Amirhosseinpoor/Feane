from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(null=True, blank=True)
    tel = models.PositiveBigIntegerField(null=True, blank=True)
    loc = models.CharField(null=True, blank=True, max_length=500)
    first_name = models.CharField(null=True, blank=True, max_length=300)
    last_name = models.CharField(null=True, blank=True, max_length=300)
# Create your models here.
