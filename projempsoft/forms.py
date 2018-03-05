from django import forms
from . import models

class CreateEstudante(forms.ModelForm):
    class Meta:
        model = models.Estudante
        fields = ('nome', 'data_nascimento', 'curso', 'conclusao', 'cep', 'endereco',
                  'cidade', 'telefone', 'descricao_curriculo', 'nome_usuario', 'senha')


class CreateEmpresa(forms.ModelForm):
    class Meta:
        model = models.Empresa
        fields = ('nome', 'endereco', 'cnpj', 'cep', 'cidade', 'telefone', 'nome_empresa',
                  'senha')