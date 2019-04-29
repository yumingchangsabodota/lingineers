from django.shortcuts import render
from django.views.generic import View
from .app_list import app_list
# Create your views here.
class HomeView(View):
	def get(self, request, *args, **kwargs):

		return render(request, 'home/home.html', {'app_list':app_list})