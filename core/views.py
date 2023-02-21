from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate
# from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from core.models import User
from .forms import UserForm
from . import gera_graficos


def home(request):
    return render(request, 'core/home.html')


# @login_required
def principal(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']        
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            request.session['access_level'] = usuario.access_level

            data_cpu = gera_graficos.consumo_cpu()
            data_memoria = gera_graficos.consumo_memoria()
            info_cluster = gera_graficos.info_cluster()

            # context = {
            #     "data_cpu": data_cpu, 
            #     "data_memoria": data_memoria, 
            #     "info_cluster": info_cluster
            # }

            return render(request, 'core/principal.html', {'data_cpu': data_cpu, 'data_memoria': data_memoria, 'info_cluster': info_cluster})
            
        return HttpResponse(request, 'core/home.html')


def gerenciamento_usuarios(request):
    return render(request, 'core/gerenciamento_usuarios.html')


def cadastro_usuario(request):
    email = request.POST['email']
    password = request.POST['password']
    access_level = request.POST['access_level']
    user = User.objects.create_user(email, password, access_level)
    user.save()
    return render(request, 'core/lista_usuarios.html')


def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'core/lista_usuarios.html', {'usuarios': usuarios})


def cadastro_usuario_teste(request):
    print('aqui grava usuário')
    form = UserForm(request.POST or None)
    if not form.is_valid():
        return render(request, 'core/cadastra_usuarios.html', {'form': form}) 
    usuario = form.save(commit=False)
    usuario.password = make_password(usuario.password)
    usuario.save()
    return redirect('core:lista-usuarios')
  

def edita_usuario(request, pk):
    user = get_object_or_404(User, pk=pk)
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('lista_usuario')
    return render(request, 'user_form.html', {'form': form})


def exclui_usuario(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('lista_usuario')
    return render(request, 'usuario_confirm_delete.html', {user: user})