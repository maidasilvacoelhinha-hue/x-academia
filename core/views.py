from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from .decorators import dono_required
from .forms import MatriculaForm, MensalidadeForm, PlanoForm, ProfessorForm
from .models import Mensalidade, Modalidade, Plano, Professor


def home(request):
    return render(
        request,
        "core/home.html",
        {
            "planos": Plano.objects.all(),
            "professores": Professor.objects.all(),
            "modalidades": Modalidade.objects.all(),
        },
    )


def sobre(request):
    return render(request, "core/sobre.html")


def planos(request):
    return render(request, "core/planos.html", {"planos": Plano.objects.all()})


def professores(request):
    return render(
        request,
        "core/professores.html",
        {"professores": Professor.objects.all()},
    )


def matricula(request):
    if request.method == "POST":
        form = MatriculaForm(request.POST)
        if form.is_valid():
            matricula_obj = form.save()
            return render(request, "core/sucesso.html", {"matricula": matricula_obj})
    else:
        form = MatriculaForm()
    return render(request, "core/matricula.html", {"form": form})


@login_required
def painel_aluno(request):
    if request.user.is_staff:
        return redirect("painel_dono")

    mensalidade, _ = Mensalidade.objects.get_or_create(
        aluno=request.user,
        defaults={"status": Mensalidade.STATUS_NAO_PAGA},
    )
    return render(
        request,
        "core/painel_aluno.html",
        {"mensalidade": mensalidade},
    )


@dono_required
def painel_dono(request):
    mensalidades = Mensalidade.objects.select_related("aluno", "plano")
    return render(
        request,
        "core/painel_dono.html",
        {
            "total_alunos": User.objects.filter(is_staff=False).count(),
            "total_professores": Professor.objects.count(),
            "total_planos": Plano.objects.count(),
            "mensalidades": mensalidades,
        },
    )


@dono_required
def gerenciar_professores(request):
    return render(
        request,
        "core/gerenciar_professores.html",
        {"professores": Professor.objects.all()},
    )


@dono_required
def cadastrar_professor(request):
    form = ProfessorForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("gerenciar_professores")
    return render(
        request,
        "core/professor_form.html",
        {"form": form, "titulo": "Cadastrar professor", "botao": "Cadastrar professor"},
    )


@dono_required
def editar_professor(request, professor_id):
    professor = get_object_or_404(Professor, id=professor_id)
    form = ProfessorForm(
        request.POST or None,
        request.FILES or None,
        instance=professor,
    )
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("gerenciar_professores")
    return render(
        request,
        "core/professor_form.html",
        {
            "form": form,
            "titulo": "Editar professor",
            "botao": "Salvar alterações",
            "professor": professor,
        },
    )


@dono_required
def excluir_professor(request, professor_id):
    professor = get_object_or_404(Professor, id=professor_id)
    if request.method == "POST":
        professor.delete()
        return redirect("gerenciar_professores")
    return render(request, "core/excluir_professor.html", {"professor": professor})


@dono_required
def gerenciar_planos(request):
    return render(
        request,
        "core/gerenciar_planos.html",
        {"planos": Plano.objects.all()},
    )


@dono_required
def cadastrar_plano(request):
    form = PlanoForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("gerenciar_planos")
    return render(
        request,
        "core/plano_form.html",
        {"form": form, "titulo": "Cadastrar plano", "botao": "Cadastrar plano"},
    )


@dono_required
def editar_plano(request, plano_id):
    plano = get_object_or_404(Plano, id=plano_id)
    form = PlanoForm(request.POST or None, instance=plano)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("gerenciar_planos")
    return render(
        request,
        "core/plano_form.html",
        {"form": form, "titulo": "Editar plano", "botao": "Salvar alterações"},
    )


@dono_required
def excluir_plano(request, plano_id):
    plano = get_object_or_404(Plano, id=plano_id)
    if request.method == "POST":
        plano.delete()
        return redirect("gerenciar_planos")
    return render(request, "core/excluir_plano.html", {"plano": plano})


@dono_required
def gerenciar_mensalidades(request):
    mensalidades = Mensalidade.objects.select_related("aluno", "plano")
    return render(
        request,
        "core/gerenciar_mensalidades.html",
        {"mensalidades": mensalidades},
    )


@dono_required
def editar_mensalidade(request, mensalidade_id):
    mensalidade = get_object_or_404(Mensalidade, id=mensalidade_id)
    form = MensalidadeForm(request.POST or None, instance=mensalidade)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("gerenciar_mensalidades")
    return render(
        request,
        "core/mensalidade_form.html",
        {"form": form, "mensalidade": mensalidade},
    )
