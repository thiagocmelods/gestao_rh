from django.shortcuts import render, redirect
from .models import Empresa
from django.views.generic.edit import CreateView, UpdateView


class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome']

    def form_valid(self, form):
        obj = form.save()
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return redirect('home')

class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome']
    