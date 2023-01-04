from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    
    path('admin/', admin.site.urls),
    path('funcionarios/', include('funcionarios.urls')),
    path('empresas/', include('empresas.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

]
