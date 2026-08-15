# X Academia — pronto para publicar no Render

Este projeto já foi preparado para rodar publicamente no Render.

## O que já está configurado

- Django 6.0.7
- Gunicorn + Uvicorn para o servidor de produção
- WhiteNoise para arquivos CSS/estáticos
- PostgreSQL via `DATABASE_URL`
- `SECRET_KEY` gerada pelo Render
- `DEBUG=False` automaticamente no Render
- `render.yaml` para criar o site e o banco de dados
- `build.sh` para instalar dependências, coletar arquivos estáticos e executar migrações

## Publicação

1. Crie um repositório no GitHub.
2. Envie **o conteúdo desta pasta** para o repositório. O arquivo `manage.py` deve ficar na raiz do repositório.
3. No Render, escolha **New Blueprint**.
4. Conecte o repositório do GitHub.
5. O Render vai ler o `render.yaml` e criar o site e o PostgreSQL.
6. Quando o deploy terminar, o site terá um endereço parecido com:
   `https://x-academia.onrender.com`

## Criar o usuário dono depois da publicação

No Render Shell, execute:

```bash
python manage.py createsuperuser
```

## Importante sobre fotos enviadas pelo site

No plano gratuito, arquivos enviados para o disco local do serviço podem desaparecer após reinicializações/deploys. Os dados salvos no PostgreSQL são separados do sistema de arquivos. Para fotos permanentes, use um serviço de armazenamento externo ou um disco persistente pago.
