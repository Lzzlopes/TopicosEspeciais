from django import forms
from .models import Tarefa
from django.contrib.auth.models import User


class TarefaForm(forms.ModelForm):
    responsavel = forms.ModelChoiceField(queryset=User.objects.all(), label="Responsável")

    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'status', 'responsavel']
