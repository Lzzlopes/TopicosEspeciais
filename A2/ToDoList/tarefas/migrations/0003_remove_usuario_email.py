# Generated by Django 4.2.16 on 2024-09-12 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0002_remove_tarefa_id_tarefa_remove_tarefa_nome_tarefa_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='email',
        ),
    ]
