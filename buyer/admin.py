from django.contrib import admin
from .models import BuyerUser
from .forms import CustomBuyerUser
from django.contrib.auth.admin import UserAdmin


class BuyerAdmin(admin.ModelAdmin):
    model = BuyerUser
    list_display = (
        'first_name',
        'last_name',
        'loc',
        'tel',
        'food_code',
        'email'
    )

admin.site.register(BuyerUser, BuyerAdmin)
# Register your models here.
