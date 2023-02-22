from django.db import models

# Create your models here.

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)

class Atendimento(models.Model):
    SERVICOS =(
        ('L', 'Limpeza profunda'),
        ('S', 'Limpeza simples')
    )
    servico = models.CharField(max_length=1, choices=SERVICOS)
    atendente = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='atendimentos_cadastrados')
    helper = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='atendimento_executados')
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    v_desconto = models.DecimalField(max_digits=8, decimal_places=2)
    PAGAMENTO = (
        ('Pix', 'Pix'),
        ('Especie','Espécie'),
        ('Debito', 'Débito'),
        ('Credito', 'Crédito')
    )
    forma_de_pagamento = models.CharField(max_length=7, choices=PAGAMENTO)
    data_cadastro = models.DateTimeField()
    data_limpeza = models.DateTimeField()
    SITUACAO =(
        ('P', 'Pendente'),
        ('R', 'Realizado'),
        ('C', 'Cancelado')
    )
    situacao = models.CharField(max_length=1, choices=SITUACAO)
    nome_cliente = models.CharField(max_length=100)
    tel_cliente = models.CharField(max_length=20)
    endereco_cliente = models.CharField(max_length=200)
