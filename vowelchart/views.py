from django.shortcuts import render
from django import forms
from django.views.generic import View
from vowelchart.vowelchart_vowel_lists import Vowel_Lists
from django.http import JsonResponse
from vowelchart.formant_analysis import Formant_analyzer
import json
# Create your views here.

class VowelChart(View):
	def get(self, request, *args, **kwargs):

		english_vowel_list = Vowel_Lists.vowel_lists['english']
		formants = Vowel_Lists.formants
		x_y = Vowel_Lists.x_y
		
		return render(request, 'vowelchart/vowelchart.html', {'formants':formants, 'x_y':x_y, 'english_vowel_list':english_vowel_list})

def getFormants(request):
	x_y = Vowel_Lists.x_y
	
	return JsonResponse(x_y)

def formant_analysis(request):

	
	if request.method == 'POST':

		print(request)
		myform = forms.Form(request.POST, request.FILES)
		vowel = request.POST.get('vowel', None)
		print(vowel)
		print("Done loading form")
		if myform.is_valid():
			print(myform.files)
			file = myform.files['audio']
			analyzer = Formant_analyzer()
			analyzer.getFormants(file)
			answer = analyzer.formants
			data = {'data':{'vowel':vowel, 'formants':answer}}

			return JsonResponse(data)