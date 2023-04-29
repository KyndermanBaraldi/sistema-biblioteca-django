from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=64)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
