from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('principal/', views.principal, name='principal'),
    # path('gerenciamento/', views.gerenciamento_usuarios, name='gerenciamento-usuarios'),
    # path('cadastro/', views.cadastro_usuario),
    path('lista-usuarios/', views.lista_usuarios, name='lista-usuarios'),
    path('cadastra-usuarios', views.cadastro_usuario_teste , name='cadastra-usuarios'),
    path('edita-usuarios/<int:pk>', views.edita_usuario , name='edita-usuarios'),
    path('exclui-usuarios/<int:pk>', views.exclui_usuario , name='exclui-usuarios'),

    # path('grafico-cluster/', views.gera_grafico_info_cluster),
]
