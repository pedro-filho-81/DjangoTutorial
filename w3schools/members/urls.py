from django.urls import path
# de members importe o arquivo views(vizualizar)
from . import views

urlpatterns = [
    path('', views.members, name='main'),
    # quando a URL FOR alguma_coisa/members, no aplicativo members, no arquivo views, exiba a função members()
    path('members/', views.members, name='members'),
    # do aplicativo members, no arquivo views, exiba a função details()
    path('members/details/<int:id>', views.details, name='details'),
]
