from django.http import Http404
from django.http import HttpResponse
from . models import Empresa, Estudante
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, "index.html")

def estudante(request):
    all_estudantes = Estudante.objects.all()
    context = {
        'all_estudantes': all_estudantes,

    }
    return render(request, "estudante.html", context)

def cadastro_estudante(request):
    return render(request, "cadastro-estudante.html")

def cadastro_empresa(request):
    return render(request, "cadastro-empresa.html")

def detail(request, estudante_id):
    estudante = get_object_or_404(Estudante, pk=estudante_id)
    return render(request, "estudante_detalhe.html", {'estudante': estudante})
