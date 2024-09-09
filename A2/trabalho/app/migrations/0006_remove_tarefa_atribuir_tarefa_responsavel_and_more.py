# Generated by Django 4.2.16 on 2024-09-09 03:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_tarefaform'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarefa',
            name='atribuir',
        ),
        migrations.AddField(
            model_name='tarefa',
            name='responsavel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_tasks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='TarefaForm',
        ),
    ]
