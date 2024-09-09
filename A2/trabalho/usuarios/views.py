from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django, logout as logout_django
from django.contrib.auth.decorators import login_required

def cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('senha')

        if User.objects.filter(email=email).exists():
            return HttpResponse('Já existe um usuário com esse e-mail')

        User.objects.create_user(username=username, email=email, password=password)
        return redirect('login')
    return render(request, 'cadastro.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('senha')
        user = authenticate(request, username=username, password=password)
        if user:
            login_django(request, user)
            return redirect('tarefasusuario', user_id=user.id)
        else:
            return HttpResponse("Email ou senha incorretos")
    return render(request, 'login.html')

@login_required(login_url='auth/login/')
def logout(request):
    logout_django(request)
    return redirect('home')
