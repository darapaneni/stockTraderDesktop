# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'stocktradingapp/home.html')

def portifolio(request):
    return render(request, 'stocktradingapp/portifolio.html')

def buy(request):
    return render(request, 'stocktradingapp/buy.html')

def purchased(request):
    return render(request, 'stocktradingapp/purchased.html')
