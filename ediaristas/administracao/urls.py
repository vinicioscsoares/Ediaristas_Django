from django.urls import path
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse_lazy
from .views import servico_views, usuario_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('servico/cadastrar', login_required(servico_views.cadastar_servico),name='cadastrar_servico'),
    path('servico/listar/', servico_views.listar_servico,name='listar_servico'),
    path('servico/editar/<int:id>', login_required(servico_views.editar_servico),name='editar_servico'),
    path('usuarios/cadastrar', usuario_views.cadastrar_usuario,name='cadastrar_usuario'),
    path('usuarios/listar/', usuario_views.listar_usuario,name='listar_usuario'),
    path('usuarios/editar/<int:id>', usuario_views.editar_usuario,name='editar_usuario'),
    path('auth/login/',auth_views.LoginView.as_view(), name='logar_usuario'),
    path('auth/logout/', auth_views.LogoutView.as_view(), name='logout_usuario'),
    path('auth/logout/sucesso/',usuario_views.logout_success, name='logout_success'),
    path('alterar_senha/',login_required(auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('senha_alterada'))),name='alterar_senha'),
    path('alterar_senha/sucesso',login_required(usuario_views.senha_alterada), name='senha_alterada'),
]
