from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import View

# Create your views here.

class FFT(View):
	def get(self, request, *args, **kwargs):
		
		return render(request, 'FFT/FFT.html')
