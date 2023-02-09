from django.db import models

# Create your models here.

class Estudante(models.Model):
    numero_estudante = models.PositiveIntegerField()
    primeiro_nome = models.CharField(max_length=50)
    segundo_nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    curso = models.CharField(max_length=50)
    media = models.FloatField()

    def __str__(self):
        return f'Estudante: {self.primeiro_nome} {self.segundo_nome}'