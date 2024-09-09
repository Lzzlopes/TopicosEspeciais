from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('auth/', include('usuarios.urls')),  # Inclui URLs do aplicativo 'usuarios'
    path('tarefas/', include('app.urls')),  # Inclui URLs do aplicativo 'app'
]
