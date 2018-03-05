from time import timezone

from django.http import Http404
from django.http import HttpResponse
from .models import Empresa, Estudante
from . import forms
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView


def index(request):
    return render(request, "index.html")


def estudante(request):
    all_estudantes = Estudante.objects.all()
    context = {
        'all_estudantes': all_estudantes,

    }
    return render(request, "estudante.html", context)


def cadastro_estudante(request):
    form = forms.CreateEstudante()
    return render(request, "cadastro-estudante.html", {'form': form})


def cadastro_empresa(request):
    form = forms.CreateEmpresa()
    return render(request, "cadastro-empresa.html", {'form': form})


def detail(request, estudante_id):
    estudante = get_object_or_404(Estudante, pk=estudante_id)
    return render(request, "estudante_detalhe.html", {'estudante': estudante})


def login(request):
    return render(request, "login.html")


def post_new_estudante(request):
    if request.method == "POST":
        form = forms.CreateEstudante(request.POST)
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('/login/')
    return render(request, 'cadastro-estudante.html')


def post_new_empresa(request):
    print("fora")
    if request.method == "POST":
        form = forms.CreateEmpresa(request.POST)
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('/login/')
    return render(request, 'cadastro-empresa.html')