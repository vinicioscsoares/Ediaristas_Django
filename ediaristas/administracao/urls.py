from django.urls import path
from .views import *

urlpatterns = [
    path('servico/cadastrar', cadastar_servico,name='cadastrar_servico'),
    path('servico/listar', listar_servico,name='listar_servico'),
]
