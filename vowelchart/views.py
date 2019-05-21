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
		vowel_list_action = [{'vowel':'a','action':'Next', 'next':'e', 'modaltitle':'Record Vowel a'},
							{'vowel':'e','action':'Next', 'next':'i', 'modaltitle':'Record Vowel e'},
							{'vowel':'i','action':'Next', 'next':'o', 'modaltitle':'Record Vowel i'},
							{'vowel':'o','action':'Next', 'next':'u', 'modaltitle':'Record Vowel o'},
							{'vowel':'u','action':'Process', 'next':'to-formants', 'modaltitle':'Record Vowel u'}]
		
		return render(request, 'vowelchart/vowelchart.html', {'formants':formants, 'x_y':x_y, 'vowel_list_action':vowel_list_action})

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