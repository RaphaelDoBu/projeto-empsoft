from django.http import Http404
from django.http import HttpResponse
from . models import Empresa, Estudante
from django.shortcuts import render

def index(request):
    all_estudantes = Estudante.objects.all()
    context = {
        'all_estudantes': all_estudantes,

    }
    return render(request, "estudante.html", context)

def detail(request, estudante_id):
    try:
        estudante = Estudante.objects.get(pk=estudante_id)
    except Estudante.DoesNotExist:
        raise Http404("Estudante nao existe")
    return render(request, "estudante_detalhe.html", {'estudante': estudante})
