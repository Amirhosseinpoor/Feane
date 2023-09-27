from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'tel',
        'loc',
        'is_staff',
    )
    add_fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('tel', 'loc')}),)
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('tel', 'loc')}),)
# Register your models here.


admin.site.register(CustomUser, CustomUserAdmin)
