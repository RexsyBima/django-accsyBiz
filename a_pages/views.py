from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

# class A_Pages:
#     class Home(TemplateView):
#         template_name = 'a_pages/home.html'


class Home(TemplateView):
    template_name = 'a_pages/home.html'
