from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def index(request):
	return render(request, 'index.html')

def login(request):
	return render(request, 'login.html')

def informacion(request):
	return render(request, 'informacion.html')

def discography(request):
	return render(request, 'discography.html')

def galery(request):
	return render(request, 'galery.html')

def fanArts(request):
	return render(request, 'fanArts.html')

def productos(request):
	return render(request, 'productos.html')
