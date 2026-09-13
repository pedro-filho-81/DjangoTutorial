from django.urls import path
from . import views

urlpatterns = [
  # inclui do arquivo views a função index quando a url vazia 
    path('', views.index, name='index')
]
