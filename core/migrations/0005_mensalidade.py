from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0004_matricula"),
    ]

    operations = [
        migrations.CreateModel(
            name="Mensalidade",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("status", models.CharField(
                    choices=[
                        ("paga", "Paga"),
                        ("nao_paga", "Não paga"),
                        ("a_expirar", "A expirar"),
                        ("cancelada", "Cancelada"),
                    ],
                    default="nao_paga",
                    max_length=20,
                )),
                ("data_inicio", models.DateField(default=django.utils.timezone.localdate)),
                ("data_vencimento", models.DateField(blank=True, null=True)),
                ("observacao", models.TextField(blank=True)),
                ("atualizado_em", models.DateTimeField(auto_now=True)),
                ("aluno", models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name="mensalidade",
                    to=settings.AUTH_USER_MODEL,
                )),
                ("plano", models.ForeignKey(
                    blank=True,
                    null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    related_name="mensalidades",
                    to="core.plano",
                )),
            ],
            options={
                "ordering": ["data_vencimento", "aluno__username"],
            },
        ),
    ]
