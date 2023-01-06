from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.FuncionariosList.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>', views.FuncionarioEdit.as_view(), name='update_funcionario'),
    path('delete/<int:pk>', views.FuncionarioDelete.as_view(), name='delete_funcionario'),
    path('add/', views.FuncionarioCreate.as_view(), name='create_funcionario'),

    
]
