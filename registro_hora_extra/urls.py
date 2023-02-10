from django.urls import path, include
from .views import HoraExtraList, HoraExtraCreate, HoraExtraEdit, HoraExtraDelete


urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('novo', HoraExtraCreate.as_view(), name='create_hora_extra'),
    path('editar/<int:pk>', HoraExtraEdit.as_view(), name='update_hora_extra'),
    path('delete/<int:pk>', HoraExtraDelete.as_view(), name='delete_hora_extra'),    
]
