from django.db import models

# Create your models here.


class Livros(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editora = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    disponivel = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Livros'
        verbose_name = 'Livro'

    def __str__(self):
        return self.titulo


class Emprestimo(models.Model):
    livro = models.ForeignKey(Livros, on_delete=models.CASCADE)
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField(blank=True, null=True)
    devolvido = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Emprestimos'
        verbose_name = 'Emprestimo'

    def __str__(self):
        return self.livro.titulo
