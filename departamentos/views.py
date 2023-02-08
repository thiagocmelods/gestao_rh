from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Departamento
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

class DepartamentosList(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)

class DepartamentoCreate(CreateView):
    model = Departamento
    fields = ['nome']
    extra_context = {'operacao':'Inserir'}

    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentoCreate, self).form_valid(form)

class DepartamentoUpdate(UpdateView):
    model = Departamento
    fields = ['nome']
    extra_context = {'operacao':'Editar'}

class DepartamentoDelete(DeleteView):
    model = Departamento
    success_url = reverse_lazy('list_departamentos')

