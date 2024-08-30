from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from ..forms.usuarios_forms import CadastroUsuarioForm, EditarUsuarioForm
from django.shortcuts import render,redirect
@login_required
def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = CadastroUsuarioForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
    else:
        form_usuario=CadastroUsuarioForm()
    return render(request,'usuarios/form_usuario.html',{'form_usuario':form_usuario})

@login_required
def listar_usuario(request):
    User=get_user_model()
    usuarios= User.objects.all()
    return render(request,'usuarios/lista_usuario.html',{'usuarios':usuarios})

@login_required
def editar_usuario(request,id):
    User=get_user_model()
    usuario=User.objects.get(id=id)
    form_usuario=EditarUsuarioForm(request.POST or None, instance=usuario)
    if form_usuario.is_valid():
        form_usuario.save()
        return redirect('listar_usuario')
    return render(request,'usuarios/form_usuario.html',{'form_usuario':form_usuario})

def senha_alterada(request):
    return render(request,'registration/success.html')

def logout_success(request):
    return render(request,'registration/logout.html')