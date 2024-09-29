from django.contrib import admin
from django.urls import path, include
from tarefas import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Mapeia a view 'home' para o caminho vazio
    path('auth/', include('tarefas.urls')),  # Inclui as URLs de login/cadastro
    path('tarefas/', views.main, name='tarefas'),  # Lista de tarefas
    path('tarefas/criar/', views.criar_tarefa, name='criar_tarefa'),  # Criação de tarefas
    path('tarefas/<int:tarefa_id>/editar/', views.editar_tarefa, name='editar_tarefa'),  # Edição de tarefas
    path('tarefas/<int:tarefa_id>/deletar/', views.deletar_tarefa, name='deletar_tarefa'),  # Exclusão de tarefas
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


]
