from django import forms
from .models import Tarefa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'status', 'responsavel']  # Inclua apenas os campos que você deseja exibir no
        # formulário
