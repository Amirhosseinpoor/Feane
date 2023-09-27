from django.urls import path
from .views import BuyerView, SuccessBuy
urlpatterns = [
    path('', BuyerView.as_view(), name='buyer'),
    path('success/', SuccessBuy.as_view(), name='success_buy')
]
