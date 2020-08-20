from django.shortcuts import render
from django.shortcuts import HttpResponse
from django import template  
from Rooms.models import room




# Create your views here.

def index(request):
    
     return render(request, 'theme/index.html')


