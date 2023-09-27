from django.shortcuts import render
from django.contrib.auth.views import TemplateView
from django.views.generic import CreateView
from .models import BuyerUser
from django.contrib.auth.views import reverse_lazy
from .forms import CustomBuyerUser

class BuyerView(CreateView):
    model = BuyerUser
    form_class = CustomBuyerUser
    success_url = reverse_lazy('success_buy')
    template_name = 'buy.html'


class SuccessBuy(TemplateView):
    template_name ='registration/success_buy.html'

# Create your views here.
