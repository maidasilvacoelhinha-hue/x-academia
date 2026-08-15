from datetime import timedelta

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Plano(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    descricao = models.TextField()

    def __str__(self):
        return self.nome


class Professor(models.Model):
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    foto = models.ImageField(upload_to="professores/", blank=True, null=True)

    def __str__(self):
        return self.nome


class Modalidade(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    icone = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nome


class Matricula(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    plano = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Mensalidade(models.Model):
    STATUS_PAGA = "paga"
    STATUS_NAO_PAGA = "nao_paga"
    STATUS_EXPIRAR = "a_expirar"
    STATUS_CANCELADA = "cancelada"

    STATUS_CHOICES = [
        (STATUS_PAGA, "Paga"),
        (STATUS_NAO_PAGA, "Não paga"),
        (STATUS_EXPIRAR, "A expirar"),
        (STATUS_CANCELADA, "Cancelada"),
    ]

    aluno = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="mensalidade",
    )
    plano = models.ForeignKey(
        Plano,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="mensalidades",
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_NAO_PAGA,
    )
    data_inicio = models.DateField(default=timezone.localdate)
    data_vencimento = models.DateField(null=True, blank=True)
    observacao = models.TextField(blank=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["data_vencimento", "aluno__username"]

    def __str__(self):
        return f"{self.aluno.username} - {self.get_status_display()}"

    @property
    def dias_para_vencer(self):
        if not self.data_vencimento:
            return None
        return (self.data_vencimento - timezone.localdate()).days

    @property
    def status_visual(self):
        if self.status == self.STATUS_CANCELADA:
            return self.STATUS_CANCELADA

        if self.data_vencimento:
            dias = self.dias_para_vencer
            if dias < 0:
                return self.STATUS_NAO_PAGA
            if 0 <= dias <= 7 and self.status == self.STATUS_PAGA:
                return self.STATUS_EXPIRAR

        return self.status

    @property
    def status_visual_label(self):
        labels = dict(self.STATUS_CHOICES)
        return labels.get(self.status_visual, self.get_status_display())
