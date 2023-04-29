from django.db import models

# Create your models here.


class Livros(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    quantidade = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Livros'
        verbose_name = 'Livro'

    def __str__(self):
        return self.titulo
