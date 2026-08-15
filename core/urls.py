from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("sobre/", views.sobre, name="sobre"),
    path("planos/", views.planos, name="planos"),
    path("professores/", views.professores, name="professores"),
    path("matricula/", views.matricula, name="matricula"),

    path("painel/aluno/", views.painel_aluno, name="painel_aluno"),
    path("painel/dono/", views.painel_dono, name="painel_dono"),

    path("gestao/professores/", views.gerenciar_professores, name="gerenciar_professores"),
    path("gestao/professores/cadastrar/", views.cadastrar_professor, name="cadastrar_professor"),
    path("gestao/professores/<int:professor_id>/editar/", views.editar_professor, name="editar_professor"),
    path("gestao/professores/<int:professor_id>/excluir/", views.excluir_professor, name="excluir_professor"),

    path("gestao/planos/", views.gerenciar_planos, name="gerenciar_planos"),
    path("gestao/planos/cadastrar/", views.cadastrar_plano, name="cadastrar_plano"),
    path("gestao/planos/<int:plano_id>/editar/", views.editar_plano, name="editar_plano"),
    path("gestao/planos/<int:plano_id>/excluir/", views.excluir_plano, name="excluir_plano"),

    path("gestao/mensalidades/", views.gerenciar_mensalidades, name="gerenciar_mensalidades"),
    path("gestao/mensalidades/<int:mensalidade_id>/editar/", views.editar_mensalidade, name="editar_mensalidade"),
]
