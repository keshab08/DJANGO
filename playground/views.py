from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def say_hello(request):
    return render(request, 'home.html', {'name': 'Ashim'})