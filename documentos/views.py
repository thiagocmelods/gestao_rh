from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Documento
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

class DocumentoList(ListView):
    model = Documento


    def get_queryset(self):
        proprietario = self.request.user.funcionario
        return Documento.objects.filter(proprietario=proprietario)

class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']
    extra_context = {'operacao':'Inserir'}

    def form_valid(self, form):
        documento = form.save(commit=False)
        documento.proprietario = self.request.user.funcionario
        documento.save()
        return super(DocumentoCreate, self).form_valid(form)

class DocumentoUpdate(UpdateView):
    model = Documento
    fields = ['descricao', 'arquivo']
    extra_context = {'operacao':'Editar'}
    success_url = reverse_lazy('list_documentos')

class DocumentoDelete(DeleteView):
    model = Documento
    success_url = reverse_lazy('list_documentos')
