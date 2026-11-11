from django.db import models

# Create your models here.
# cria a classe para os membros do clube
class Member(models.Model):
    # cria o campo primeiro nome para 255 caracteres
    firstName = models.CharField(max_length=255)
    # cria o campo último nome para 255 caracteres
    lastName = models.CharField(max_length=255)
    # cria o campo para o telefone
    phone = models.IntegerField(null=True)
    # cria o campo para data
    joined_date = models.DateField(null=True)
