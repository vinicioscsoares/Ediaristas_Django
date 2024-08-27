from django.contrib.auth import get_user_model
from ..forms.usuarios_forms import UsuarioForm
from django.shortcuts import render

def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UsuarioForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
    else:
        form_usuario=UsuarioForm()
    return render(request,'usuarios/form_usuario.html',{'form_usuario':form_usuario})

def listar_usuario(request):
    User=get_user_model()
    usuarios= User.objects.all()
    return render(request,'usuarios/lista_usuario.html',{'usuarios':usuarios})