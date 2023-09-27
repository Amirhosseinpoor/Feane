from django.db import models

class BuyerUser(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=False)
    last_name = models.CharField(max_length=255, null=True, blank=False)
    food_code = models.PositiveIntegerField(null=True, blank=False)
    loc = models.CharField(max_length=255, blank=False, null=True)
    tel = models.CharField(max_length=255, blank=False, null=True)
    email = models.EmailField(blank=False, null=True)




# Create your models here.
