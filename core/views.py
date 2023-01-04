from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from funcionarios.models import Funcionario

@login_required(login_url='login')
def home(request):
    usuario = request.user
    context = {
        'usuario':usuario
    }
    return render(request, 'core/index.html', context)
