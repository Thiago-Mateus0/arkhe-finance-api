# Arkhé Finance API

> API REST de controle financeiro pessoal — desenvolvida do zero por um estudante de Ciência da Computação.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?style=flat-square)
![SQLite](https://img.shields.io/badge/SQLite-lightgrey?style=flat-square)
![Render](https://img.shields.io/badge/Deployed%20on-Render-00b3b0?style=flat-square&logo=render)
![Status](https://img.shields.io/badge/status-ativo-brightgreen?style=flat-square)

---

## 🚀 Deploy e Acesso

A API está em produção e pode ser acessada publicamente.

| Ambiente | URL |
|---|---|
| **API (Produção)** | [https://arkhe-finance-api.onrender.com](https://arkhe-finance-api.onrender.com) |
| **Documentação (Swagger)** | [https://arkhe-finance-api.onrender.com/docs](https://arkhe-finance-api.onrender.com/docs) |

---

## Sobre o projeto

O Arkhé Finance API centraliza o controle financeiro pessoal via HTTP. Permite registrar entradas e saídas, organizar por categorias, filtrar transações e visualizar um resumo financeiro consolidado.

Desenvolvido como projeto de portfólio durante o primeiro semestre de Ciência da Computação, com foco em fundamentos reais de backend e arquitetura de APIs.

---

## Tecnologias

| Ferramenta | Uso |
|---|---|
| **Python 3** | Linguagem principal |
| **FastAPI** | Framework da API |
| **SQLite** | Banco de dados (Persistência local) |
| **Uvicorn** | Servidor ASGI |
| **Render** | Plataforma de Hospedagem (PaaS) |

---

## Como executar localmente

```bash
# Clonar o repositório
git clone [https://github.com/Thiago-Mateus0/arkhe-finance-api](https://github.com/Thiago-Mateus0/arkhe-finance-api)
cd arkhe-finance-api

# Configurar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependências
pip install fastapi uvicorn

# Executar a API
python -m uvicorn main:app --reload
