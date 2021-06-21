from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Filtragem(models.Model):
    avaliador = models.IntegerField(null=False)
    arquivo = models.CharField(max_length=50, default="")
    histograma = models.CharField(max_length=2000, null=False, default="")
    gamma_l = models.FloatField(default=0.01, null=False)
    gamma_h = models.FloatField(default=1.0, null=False)
    c = models.FloatField(default=0.0, null=False)
    d0 = models.IntegerField(default=30, null=False)
    data_add = models.DateTimeField(editable=False, default=timezone.now())

    def __str__(self):
        nome = User.objects.filter(id = self.avaliador).values('first_name')
        return nome + ' - ' + self.arquivo + ' em ' + self.data_add
