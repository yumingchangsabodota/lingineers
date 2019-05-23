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
		
		return render(request, 'vowelchart/vowelchart.html', {'english_vowel_list':english_vowel_list})

def getFormants(request):
	dummy_formants = Vowel_Lists.dummy_formants
	
	return JsonResponse(dummy_formants)

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