from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from core.models import Mensalidade
from .forms import CadastroAlunoForm


def cadastro(request):
    if request.user.is_authenticated:
        return redirect("painel_aluno")

    if request.method == "POST":
        form = CadastroAlunoForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data["senha"])
            usuario.is_staff = False
            usuario.is_superuser = False
            usuario.save()

            Mensalidade.objects.get_or_create(
                aluno=usuario,
                defaults={"status": Mensalidade.STATUS_NAO_PAGA},
            )

            login(request, usuario)
            return redirect("painel_aluno")
    else:
        form = CadastroAlunoForm()

    return render(request, "alunos/cadastro.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect("painel_dono")
        return redirect("painel_aluno")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            if usuario.is_staff:
                return redirect("painel_dono")
            return redirect("painel_aluno")
    else:
        form = AuthenticationForm()

    return render(request, "alunos/login.html", {"form": form})
