from django.db import models
from django.urls import reverse
from funcionarios.models import Funcionario

class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    proprietario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, blank=True)
    arquivo = models.FileField(upload_to='documentos')

    def __str__(self):
        return self.descricao

    def get_absolute_url(self):
        return reverse('list_documentos')
