from django import forms

from django.contrib.auth.models import User

from .models import Matricula, Mensalidade, Plano, Professor


class MatriculaForm(forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ["nome", "email", "telefone", "plano"]


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ["nome", "especialidade", "descricao", "foto"]
        widgets = {
            "descricao": forms.Textarea(attrs={"rows": 5}),
            "foto": forms.ClearableFileInput(attrs={"accept": "image/*"}),
        }


class PlanoForm(forms.ModelForm):
    class Meta:
        model = Plano
        fields = ["nome", "preco", "descricao"]
        widgets = {
            "preco": forms.NumberInput(attrs={"step": "0.01", "min": "0"}),
            "descricao": forms.Textarea(attrs={"rows": 5}),
        }


class MensalidadeForm(forms.ModelForm):
    class Meta:
        model = Mensalidade
        fields = [
            "aluno",
            "plano",
            "status",
            "data_inicio",
            "data_vencimento",
            "observacao",
        ]
        widgets = {
            "data_inicio": forms.DateInput(attrs={"type": "date"}),
            "data_vencimento": forms.DateInput(attrs={"type": "date"}),
            "observacao": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["aluno"].queryset = User.objects.filter(
            is_staff=False,
            is_superuser=False,
        ).order_by("username")
