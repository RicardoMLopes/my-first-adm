from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone


class Pessoa(models.Model):
    nome        = models.CharField(max_length=200)
    GENDER_CHOICES = (
        ('F', 'Física'),
        ('J', 'Jurítica'),
    )
    tipo = models.CharField(max_length=1, choices=GENDER_CHOICES)
    cpfcnpj     = models.CharField(max_length=14)
    logradouro  = models.CharField(max_length=100)
    bairro      = models.CharField(max_length=40)
    cidade      = models.CharField(max_length=800)
    cep         = models.CharField(max_length=10)
    numero      = models.CharField(max_length=6)
    estado      = models.CharField(max_length=2)
    ibge        = models.CharField(max_length=8)
    telefone    = models.CharField(max_length=13)
    email       = models.CharField(max_length=80)
    observacao  = models.TextField()

    created_date   = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nome
