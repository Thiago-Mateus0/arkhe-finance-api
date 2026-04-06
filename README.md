# Arkhé Finance API

> API REST de controle financeiro pessoal — desenvolvida do zero por um estudante de Ciência da Computação.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?style=flat-square)
![SQLite](https://img.shields.io/badge/SQLite-lightgrey?style=flat-square)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow?style=flat-square)

---

## Sobre o projeto

O Arkhé Finance API centraliza o controle financeiro pessoal via HTTP. Permite registrar entradas e saídas, organizar por categorias, filtrar transações e visualizar um resumo financeiro consolidado.

Desenvolvido como projeto de portfólio durante o primeiro semestre de Ciência da Computação, com foco em fundamentos reais de backend.

---

## Tecnologias

| Ferramenta | Uso |
|---|---|
| Python 3 | Linguagem principal |
| FastAPI | Framework da API |
| SQLite | Banco de dados |
| Uvicorn | Servidor ASGI |

---

## Como executar
```bash
git clone https://github.com/Thiago-Mateus0/arkhe-finance-api
cd arkhe-finance-api
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
python -m uvicorn main:app --reload
```

| URL | Descrição |
|---|---|
| `http://127.0.0.1:8000` | API |
| `http://127.0.0.1:8000/docs` | Documentação interativa (Swagger) |

---

## Endpoints

### Transações

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/transacoes` | Lista todas |
| `GET` | `/transacoes?tipo=entrada` | Filtra por tipo |
| `GET` | `/transacoes?categoria_id=1` | Filtra por categoria |
| `GET` | `/transacoes?data_inicio=YYYY-MM-DD&data_fim=YYYY-MM-DD` | Filtra por período |
| `POST` | `/transacoes` | Cria nova |
| `PUT` | `/transacoes/{id}` | Atualiza |
| `DELETE` | `/transacoes/{id}` | Remove |

### Categorias

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/categorias` | Lista todas |
| `POST` | `/categorias` | Cria nova |
| `DELETE` | `/categorias/{id}` | Remove |

### Dashboard

| Método | Rota | Descrição |
|---|---|---|
| `GET` | `/dashboard` | Resumo financeiro completo |

---

## Exemplos

**Criar categoria**
```json
{
  "nome": "Alimentação",
  "tipo": "saida"
}
```

**Criar transação**
```json
{
  "tipo": "saida",
  "valor": 120.50,
  "descricao": "Supermercado",
  "categoria_id": 1,
  "data": "2026-04-06"
}
```

**Resposta do dashboard**
```json
{
  "entradas": 3000.00,
  "saidas": 850.00,
  "saldo": 2150.00,
  "gastos_por_categoria": [
    { "nome": "Alimentação", "total": 450.00 },
    { "nome": "Transporte", "total": 400.00 }
  ]
}
```

---

## Estrutura do projeto
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

---

## Melhorias futuras

- [ ] Autenticação com JWT
- [ ] Paginação de resultados
- [ ] Testes automatizados
- [ ] Deploy da API
- [ ] Validações avançadas com Pydantic

---

## Autor

**Thiago Mateus** — estudante de Ciência da Computação com foco em desenvolvimento backend.

[![GitHub](https://img.shields.io/badge/GitHub-Thiago--Mateus0-black?style=flat-square&logo=github)](https://github.com/Thiago-Mateus0)

> *"Be water, my friend."* — Bruce Lee
