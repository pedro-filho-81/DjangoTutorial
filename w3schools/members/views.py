from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# de models.py importe a classe member 
from .models import Member

# Create your views here.
def members(request):
    # mymembers recebe os valores cadastrados no banco de dados
    mymembers = Member.objects.all().values()
    # templates recebe a página Html 
    templates = loader.get_template('all_members.html')
    context = {'mymembers': mymembers,}   
    return HttpResponse(templates.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    templates = loader.get_template('details.html')
    context = {'mymember': mymember,}
    return HttpResponse(templates.render(context, request)) 

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
    