from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Usuarios(models.Model):
    id_Usuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=50)


class Tarefa(models.Model):
    id_Tarefa = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    status_escolha = [
        ('Pendente', 'Pendente'),
        ('Em progresso', 'Em progresso'),
        ('Completado', 'Completado'),
    ]
    status = models.CharField(max_length=20, choices=status_escolha, default='Pendente')
    responsavel = models.ForeignKey(User, related_name='assigned_tasks', on_delete=models.CASCADE, null=True,
                                    blank=True)


