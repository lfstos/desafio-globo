# import requests
from django.shortcuts import render
from django.contrib.auth import authenticate
# from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from core.models import User
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

            data_cpu = gera_graficos._consumo_cpu()
            data_memoria = gera_graficos._consumo_memoria()
            info_cluster = gera_graficos._info_cluster

            # context = {
            #     'data_cpu': data_cpu,
            #     'data_memoria': data_memoria
            # }

            print(info_cluster)

            return render(request, 'core/principal.html', {'data_cpu': data_cpu, 'data_memoria': data_memoria, 'data_cluster': info_cluster})
            
        return HttpResponse(request, 'core/home.html')


def gerenciamento_usuarios(request):
    return render(request, 'core/gerenciamento_usuarios.html')


def cadastro_usuario(request):
    email = request.POST['email']
    password = request.POST['password']
    access_level = request.POST['access_level']
    user = User.objects.create_user(email, password, access_level)
    user.save()
    return render(request, 'core/teste.html')


