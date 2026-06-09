# copa2026

API desenvolvida para gerenciamento de seleções e jogadores da Copa do Mundo 2026

## Executar Localmente

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Acesse:

```text
http://127.0.0.1:8000/api/selecoes/
http://127.0.0.1:8000/api/jogadores/
```

## Executar com Docker

```bash
docker build -t copa2026-api .
docker run -p 8000:8000 copa2026-api
```

## GitHub

https://github.com/SEU_USUARIO/copa2026-api

## Docker Hub

https://hub.docker.com/r/ecobs/copa2026-api
