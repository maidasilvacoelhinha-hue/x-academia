# X Academia — versão organizada

## O que foi melhorado
- Layout responsivo para celular, tablet e computador.
- Cabeçalho e navegação reorganizados.
- Página inicial com hero, diferenciais, modalidades, planos, equipe, depoimentos e CTA.
- Páginas de Sobre, Planos, Professores e Matrícula com visual consistente.
- Formulário de matrícula corrigido e conectado ao banco.
- Cadastro, login e logout de alunos corrigidos.
- Senhas de usuários continuam sendo armazenadas com o sistema de hash do Django.
- Configuração de mídia para fotos dos professores em desenvolvimento.
- CSS reorganizado com variáveis, componentes reutilizáveis e breakpoints.
- Ambiente virtual removido do ZIP para evitar um projeto enorme e difícil de transportar.

## Como executar

No terminal, dentro da pasta que contém `manage.py`:

```bash
python -m pip install django pillow
python manage.py migrate
python manage.py runserver
```

Abra `http://127.0.0.1:8000/`.

Para cadastrar dados de planos, professores e modalidades:
```bash
python manage.py createsuperuser
```
Depois acesse `/admin/`.


## Cadastro de professores sem Django Admin

Após entrar com uma conta cadastrada no site, acesse:

`http://127.0.0.1:8000/professores/gerenciar/`

Nessa página você poderá:
- cadastrar professores;
- enviar foto;
- editar informações;
- excluir professores.

Não é necessário usar `/admin/`.


## Perfis de acesso

### Dono
Crie somente uma conta de dono com:

```bash
python manage.py createsuperuser
```

Essa conta terá `is_staff=True` e verá o painel do dono em:

`/painel/dono/`

O dono pode:
- cadastrar, editar e excluir planos;
- cadastrar, editar e excluir professores;
- consultar todos os alunos;
- atualizar plano, vencimento e status das mensalidades.

### Alunos
Os alunos criam a própria conta pela página `/alunos/cadastro/`.
Eles são criados como usuários comuns e não podem acessar a gestão.

Cada aluno vê apenas a própria mensalidade em:

`/painel/aluno/`

### Status
- Paga
- Não paga
- A expirar
- Cancelada

Quando uma mensalidade paga estiver a até 7 dias do vencimento, o painel mostrará automaticamente "A expirar".
Quando o vencimento passar, mostrará "Não paga".
