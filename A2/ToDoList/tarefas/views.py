from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as login_django
from django.contrib.auth.decorators import login_required
from .models import Tarefa
from .forms import TarefaForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def cadastro(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return HttpResponse('usuario ja existe')

        user = User.objects.create_user(username, password)
        user.save()

        return redirect('tarefas')
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login_django(request, user)
            return redirect('tarefas')
        else:
            return HttpResponse('Usuário ou senha inválidos.')

    return render(request, 'tarefas.html')


@login_required(login_url='/auth/login')
def main(request):
    status_filter = request.GET.get('status', '')

    if status_filter:
        tarefas = Tarefa.objects.filter(responsavel=request.user, status=status_filter)
    else:
        tarefas = Tarefa.objects.filter(responsavel=request.user)

    return render(request, 'tarefas.html', {'tasks': tarefas})


@login_required(login_url='/auth/login')
def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarefas')
    else:
        form = TarefaForm()
    return render(request, 'criarTarefa.html', {'form': form})



@login_required
def editar_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('tarefas')
    else:
        form = TarefaForm(instance=tarefa)
    return render(request, 'editarTarefa.html', {'form': form, 'tarefa': tarefa})


@login_required
def deletar_tarefa(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id, responsavel=request.user)

    if request.method == 'POST':
        tarefa.delete()
        return redirect('tarefas')

    return render(request, 'deletarTarefa.html', {'tarefa': tarefa})


@login_required
def dashboard(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'dashboard.html', {'tarefas': tarefas})