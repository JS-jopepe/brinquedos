from django.db import models

# Create your models here.
class pedido(models.Model):
    nome = models.CharField(max_length=20)
    