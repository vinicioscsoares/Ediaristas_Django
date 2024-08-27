from django.urls import path
from .views import *


urlpatterns = [
    path('servico/cadastrar', cadastar_servico,name='cadastrar_servico'),
    path('servico/listar', listar_servico,name='listar_servico'),
    path('servico/editar/<int:id>', editar_servico,name='editar_servico'),
    path('usuarios/cadastrar', cadastrar_usuario,name='cadastrar_usuario'),
]
