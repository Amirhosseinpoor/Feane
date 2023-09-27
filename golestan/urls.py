from django.urls import path
from .views import GolestanView
from .views import AboutUsView
from .views import ReadMoreView
from .views import UserInfView
urlpatterns = [
    path('', GolestanView.as_view(), name='home'),
    path('aboutus/', AboutUsView.as_view(), name='aboutus'),
    path('readmore/',ReadMoreView.as_view(), name='readmore'),
    path('userinf/', UserInfView.as_view(), name='userinf')
]