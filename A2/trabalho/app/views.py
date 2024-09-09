from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .forms import TarefaForm
from .models import Tarefa


def home(request):
    return render(request, 'home.html')


@login_required(login_url='auth/login/')
def tarefasusuario(request, user_id):
    usuario = get_object_or_404(User, id=user_id)
    tarefas = Tarefa.objects.filter(responsavel=usuario)  # Filtra tarefas para o usuário logado

    # Filtragem de tarefas por status, se um status for passado como parâmetro na URL
    status_filter = request.GET.get('status')
    if status_filter:
        tarefas = tarefas.filter(status=status_filter)

    return render(request, 'Tarefas.html', {'tarefas': tarefas, 'user': usuario})


@login_required(login_url='auth/login/')
def criartarefa(request, user_id):
    usuario = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.user = usuario
            tarefa.save()
            return redirect('tarefasusuario', user_id=usuario.id)  # Corrigido para 'tarefasUsuario'
    else:
        form = TarefaForm()
    return render(request, 'Tarefas.html', {'create_form': form, 'user': usuario})


@login_required(login_url='auth/login/')
def editartarefa(request, user_id, idTarefa):
    usuario = get_object_or_404(User, id=user_id)
    tarefa = get_object_or_404(Tarefa, id_Tarefa=idTarefa, user=usuario)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('tarefasUsuario', user_id=usuario.id)  # Corrigido para 'tarefasUsuario'
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'Tarefas.html', {'edit_form': form, 'user': usuario})


@login_required(login_url='auth/login/')
def removertarefa(request, user_id, task_id):
    usuario = get_object_or_404(User, id=user_id)
    tarefa = get_object_or_404(Tarefa, id_Tarefa=task_id, user=usuario)
    if request.method == 'POST':
        tarefa.delete()
        return redirect('tarefas', user_id=usuario.id)
    return render(request, 'Tarefas.html', {'user': usuario})

@login_required(login_url='auth/login/')
def dashboard(request):
    tarefas = Tarefa.objects.all()  # Obtém todas as tarefas

    # Filtragem de tarefas por status, se um status for passado como parâmetro na URL
    status_filter = request.GET.get('status')
    if status_filter:
        tarefas = tarefas.filter(status=status_filter)

    return render(request, 'dashboard.html', {'tarefas': tarefas})
