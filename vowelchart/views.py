from django.shortcuts import render
from django import forms
from django.views.generic import View
from vowelchart.dummy_formants import Formants
from django.http import JsonResponse
from vowelchart.formant_analysis import Formant_analyzer
import json
# Create your views here.

class VowelChart(View):
	def get(self, request, *args, **kwargs):
		formants = Formants.formants
		x_y = Formants.x_y
		
		return render(request, 'vowelchart/vowelchart.html', {'formants':formants, 'x_y':x_y})

def getFormants(request):
	x_y = Formants.x_y
	
	return JsonResponse(x_y)

def formant_analysis(request):

	
	if request.method == 'POST':
		print('Inside imageVerify')
		print(request)
		myform = forms.Form(request.POST, request.FILES)
		print("Done loading form")
		if myform.is_valid():
			print(myform.files)
			file = myform.files['audio']
			analyzer = Formant_analyzer()
			analyzer.getFormants(file)
			answer = analyzer.formants
			data = {'data':answer}

			return JsonResponse(data)