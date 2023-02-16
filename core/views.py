from django.shortcuts import render
from django.contrib.auth import authenticate
from core.models import User


def home(request):
    return render(request, 'core/home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']        
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            request.session['access_level'] = usuario.access_level
            request.session['username'] = usuario.email
            return render(request, 'core/principal.html')
        return render(request, 'core/home.html')


def gerenciamento_usuarios(request):
    return render(request, 'core/tela_gerenciamento_usuarios.html')


def cadastro_usuario(request):
    email = request.POST['email']
    password = request.POST['password']
    access_level = request.POST['access_level']
    user = User.objects.create_user(email, password, access_level)
    user.save()
    return render(request, 'core/teste.html')
