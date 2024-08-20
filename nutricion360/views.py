from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    return render(request, 'login.html')
def aside_1(request):
    return render(request, 'aside_1.html')
def aside_2(request):
    return render(request, 'aside_2.html')
def navBar(request):
    return render(request, 'navBar.html')
def price(request):
    return render(request, 'price.html')

def pacientesList(request):
    return render(request, 'pacientesList.html')
