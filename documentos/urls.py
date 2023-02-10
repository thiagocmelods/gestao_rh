from django.urls import path
from .views import DocumentoCreate, DocumentoUpdate, DocumentoDelete, DocumentoList

urlpatterns = [    
    path('list', DocumentoList.as_view(), name="list_documentos"),
    path('novo', DocumentoCreate.as_view(), name="create_documento" ),
    path('update/<int:pk>', DocumentoUpdate.as_view(), name="update_documento" ),
    path('delete/<int:pk>', DocumentoDelete.as_view(), name="delete_documento" ),
]