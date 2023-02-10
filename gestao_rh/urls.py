from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('core.urls')),    
    path('admin/', admin.site.urls),
    path('funcionarios/', include('funcionarios.urls')),
    path('departamentos/', include('departamentos.urls')),
    path('documentos/', include('documentos.urls')),
    path('horas-extras/', include('registro_hora_extra.urls')),
    path('empresas/', include('empresas.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
