from django.shortcuts import render
from django.views.generic import TemplateView


class GolestanView(TemplateView):
    template_name = 'home.html'

class AboutUsView(TemplateView):
    template_name = 'aboutus.html'

class ReadMoreView(TemplateView):
    template_name = 'readmore.html'

class UserInfView(TemplateView):
    template_name = 'userinf.html'
# Create your views here.
