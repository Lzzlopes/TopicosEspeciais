from django.urls import path
from . import views

urlpatterns = [
    path('', views.tarefasusuario, name='tarefasusuario'),
    path('<int:user_id>/', views.tarefasusuario, name='tarefasusuario'),
    path('<int:user_id>/create/', views.criartarefa, name='create_task'),
    path('<int:user_id>/edit/<int:idTarefa>/', views.editartarefa, name='edit_task'),
    path('<int:user_id>/delete/<int:idTarefa>/', views.removertarefa, name='delete_task'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
