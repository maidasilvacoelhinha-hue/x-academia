from django import forms
from django.contrib.auth.models import User


class CadastroAlunoForm(forms.ModelForm):
    senha = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(attrs={
            "placeholder": "Crie uma senha",
            "autocomplete": "new-password",
        }),
        min_length=6,
    )

    class Meta:
        model = User
        fields = ["username", "email", "senha"]
        labels = {
            "username": "Nome de usuário",
            "email": "E-mail",
        }
        widgets = {
            "username": forms.TextInput(attrs={
                "placeholder": "Escolha um nome de usuário",
                "autocomplete": "username",
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "seuemail@exemplo.com",
                "autocomplete": "email",
            }),
        }

    def clean_email(self):
        email = self.cleaned_data["email"].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("Este e-mail já está cadastrado.")
        return email

    def clean_username(self):
        username = self.cleaned_data["username"].strip()
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("Este nome de usuário já está em uso.")
        return username
