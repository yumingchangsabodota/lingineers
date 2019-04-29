from django.shortcuts import render

# Create your views here.
def vowelchart(request):
	return render(request, 'vowelchart/vowelchart.html')
