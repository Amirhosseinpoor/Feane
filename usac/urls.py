from django.urls import path
from .views import UsacView
urlpatterns = [
    path('', UsacView.as_view(), name='signup'),
]
