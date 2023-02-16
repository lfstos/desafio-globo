from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login', views.login),
    path('gerenciamento', views.gerenciamento_usuarios),
    path('cadastro', views.cadastro_usuario),
]
