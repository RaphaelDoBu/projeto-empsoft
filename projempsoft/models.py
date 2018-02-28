from django.db import models

class Estudante(models.Model):
    nome = models.CharField(max_length= 250)
    data_nascimento = models.CharField(max_length= 250)
    curso = models.CharField(max_length= 250)
    conclusao = models.CharField(max_length= 250)
    cep = models.CharField(max_length=250)
    endereco = models.CharField(max_length=250)
    cidade = models.CharField(max_length=250)
    telefone = models.CharField(max_length=250)
    descricao_curriculo = models.CharField(max_length= 250)
    nome_usuario = models.CharField(max_length=250)
    senha = models.CharField(max_length=250)

    def __str__(self):
        return self.nome + ' - ' + self.curso

class Empresa(models.Model):
    estudante = models.ForeignKey(Estudante, on_delete=models.CASCADE)
    nome = models.CharField(max_length=250)
    endereco = models.CharField(max_length=250)
    cnpj = models.CharField(max_length=250)
    cep = models.CharField(max_length=250)
    cidade = models.CharField(max_length=250)
    telefone = models.CharField(max_length=250)
    nome_empresa = models.CharField(max_length=250)
    senha = models.CharField(max_length=250)

    def __str__(self):
        return self.nome
