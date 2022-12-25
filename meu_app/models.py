from django.db import models

# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=225)
    cpf = models.CharField(max_length=15)
    idade = models.IntegerField()
    turma = models.CharField(max_length=50)
    matricula = models.IntegerField()
    telefone = models.IntegerField(null=True)

    def __str__(self):
        return self.nome.capitalize().strip()
