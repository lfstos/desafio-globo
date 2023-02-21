from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'core'

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='core/home.html'), name='home'),
    path('principal/', views.principal, name='principal'),
    path('gerenciamento/', views.gerenciamento_usuarios),
    # path('cadastro/', views.cadastro_usuario),
    path('lista-usuarios/', views.lista_usuarios, name='lista-usuarios'),
    path('cadastra-usuarios', views.cadastro_usuario_teste , name='cadastra-usuarios'),
    path('edita-usuarios/<int:pk>', views.edita_usuario , name='edita-usuarios'),
    path('exclui-usuarios/<int:pk>', views.exclui_usuario , name='exclui-usuarios'),

    # path('grafico-cpu/', views.gera_grafico_consumo_cpu),
    # path('grafico-cluster/', views.gera_grafico_info_cluster),
]
