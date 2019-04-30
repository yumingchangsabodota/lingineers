from django.shortcuts import render
from django.views.generic import View
from vowelchart.dummy_formants import Formants
from django.http import JsonResponse
# Create your views here.

class VowelChart(View):
	def get(self, request, *args, **kwargs):
		formants = Formants.formants
		x_y = Formants.x_y
		
		return render(request, 'vowelchart/vowelchart.html', {'formants':formants, 'x_y':x_y})

def getFormants(request):
	x_y = Formants.x_y
	
	return JsonResponse(x_y)