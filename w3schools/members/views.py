from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def members(request):
    templates = loader.get_template('myFirst.html')
    return HttpResponse(templates.render())
