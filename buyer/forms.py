from django import forms
from .models import BuyerUser
class CustomBuyerUser(forms.ModelForm):
    class Meta:
        model = BuyerUser
        fields = ('first_name', 'last_name', 'food_code', 'loc', 'tel','email')
