from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from ..forms import ServicoForm
from ..models import Servico

# Create your views here.
@login_required
def cadastar_servico(request):
    if request.method=="POST":
        form_servico = ServicoForm(request.POST)
        if form_servico.is_valid():
            form_servico.save()
            return redirect('listar_servico')
    else:
        form_servico = ServicoForm()
    return render(request, 'servicos/form_servico.html', {"form_servico": form_servico})

def listar_servico(request):
    servicos= Servico.objects.all()

    return render(request,'servicos/lista_servico.html', {'servicos': servicos})
@login_required
def editar_servico(request, id):
    servico = Servico.objects.get(id=id)
    form_servico= ServicoForm(request.POST or None, instance=servico)
    if form_servico.is_valid():
        form_servico.save()
        return redirect('listar_servico')
    return render(request, 'servicos/form_servico.html', {'form_servico':form_servico})