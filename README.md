# Arkhé Finance API

> API REST de controle financeiro pessoal — desenvolvida do zero por um estudante de Ciência da Computação.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?style=flat-square)
![SQLite](https://img.shields.io/badge/SQLite-lightgrey?style=flat-square)
![Render](https://img.shields.io/badge/Deployed%20on-Render-00b3b0?style=flat-square&logo=render)
![Status](https://img.shields.io/badge/status-ativo-brightgreen?style=flat-square)

---

## 🚀 Deploy e Acesso

| Ambiente | URL |
| :--- | :--- |
| **API (Produção)** | [https://arkhe-finance-api.onrender.com](https://arkhe-finance-api.onrender.com) |
| **Documentação (Swagger)** | [https://arkhe-finance-api.onrender.com/docs](https://arkhe-finance-api.onrender.com/docs) |

---

## Sobre o Projeto

O Arkhé Finance API centraliza o controle financeiro pessoal via HTTP. Permite registrar entradas e saídas, organizar por categorias, filtrar transações e visualizar um resumo financeiro consolidado.

---

## 🛠️ Tecnologias

| Ferramenta | Uso |
| :--- | :--- |
| **Python 3** | Linguagem principal |
| **FastAPI** | Framework da API |
| **SQLite** | Banco de dados |
| **Uvicorn** | Servidor ASGI |
| **Render** | Plataforma de hospedagem |

---

## 📋 Endpoints

### Transações
| Método | Rota | Descrição |
| :--- | :--- | :--- |
| GET | `/transacoes` | Lista todas |
| GET | `/transacoes?tipo=entrada` | Filtra por tipo |
| POST | `/transacoes` | Cria nova |
| PUT | `/transacoes/{id}` | Atualiza |
| DELETE | `/transacoes/{id}` | Remove |

### Dashboard
| Método | Rota | Descrição |
| :--- | :--- | :--- |
| GET | `/dashboard` | Resumo financeiro |

---

## 🧪 Como Executar

```bash
git clone https://github.com/Thiago-Mateus0/arkhe-finance-api
cd arkhe-finance-api
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
python -m uvicorn main:app --reload
```

---

## 📁 Estrutura do Projeto

```
arkhe-finance-api/
├── app/
│   ├── database.py
│   └── routes/
│       ├── transacoes.py
│       ├── categorias.py
│       └── dashboard.py
├── main.py
├── .gitignore
└── README.md
```

---

## 🔄 Melhorias Futuras

- [x] Deploy da API (Render)a
- [ ] Migração para PostgreSQL
- [ ] Autenticação com JWT
- [ ] Testes automatizados com Pytest
- [ ] Validações avançadas com Pydantic

---

**Autor:** Thiago Mateus — Estudante de Ciência da Computação