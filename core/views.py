from django.shortcuts import render
from django.contrib.auth import authenticate
# from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'core/home.html')

# @login_required
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            return render(request, 'core/autenticacao.html')
        return render(request, 'core/home.html')
    