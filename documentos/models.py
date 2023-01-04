from django.db import models
from funcionarios.models import Funcionario

class Documento(models.Model):
    descricao = models.CharField(max_length=100, help_text='Descrição do documento')
    proprietario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.descricao
