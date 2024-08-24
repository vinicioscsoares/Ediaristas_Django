from django.shortcuts import render
from .forms import ServicoForm

# Create your views here.

def cadastar_servico(request):
    form_servico = ServicoForm()
    return render(request, 'servicos/form_servico.html', {"form_servico": form_servico})
