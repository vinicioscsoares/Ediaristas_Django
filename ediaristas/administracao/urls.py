from django.urls import path
from .views import servico_views, usuario_views


urlpatterns = [
    path('servico/cadastrar', servico_views.cadastar_servico,name='cadastrar_servico'),
    path('servico/listar', servico_views.listar_servico,name='listar_servico'),
    path('servico/editar/<int:id>', servico_views.editar_servico,name='editar_servico'),
    path('usuarios/cadastrar', usuario_views.cadastrar_usuario,name='cadastrar_usuario'),
]
