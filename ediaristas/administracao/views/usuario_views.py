from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect

def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form.is_valid():
            form_usuario.save()
    else:
        form_usuario=UserCreationForm()
    return render(request,'usuarios/form_usuario.html',{'form_usuario':form_usuario})