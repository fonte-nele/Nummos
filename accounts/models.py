from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Empresa(models.Model):
    nameResp = models.CharField(max_length=200)
    nameEst = models.CharField(max_length=200)
    segmento = models.CharField(max_length=50)
    faturamento = models.FloatField(default=0.00)
    cidade = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    senha = models.CharField(max_length=200)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Games_fbv:Game_edit', kwargs={'pk': self.pk})