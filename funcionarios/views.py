from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Funcionario
from django.contrib.auth.models import User


class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome','departamentos']
    extra_context = {'operacao':'Edit'}


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome','departamentos']
    extra_context = {'operacao':'Inserir'}

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        funcionario.empresa = self.request.user.funcionario.empresa
        username = ''
        if len(funcionario.nome.split(' ')) > 1:
            username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        else:
            username = funcionario.nome.split(' ')[0]
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        print(funcionario)
        return super(FuncionarioCreate, self).form_valid(form)
