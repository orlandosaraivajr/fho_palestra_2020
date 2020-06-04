from django.db import models
from django.utils import timezone

class FeriadoModel(models.Model):
    nome = models.CharField('Feriado', max_length=50)
    dia = models.IntegerField('Data')
    mes = models.IntegerField('Mês')
    modificado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
