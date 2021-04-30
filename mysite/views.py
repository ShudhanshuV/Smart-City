from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	return render(request,'index.html')
	
def reg(request):
	# return HttpResponse('Hello registration page')
	return render(request,'registration.html')