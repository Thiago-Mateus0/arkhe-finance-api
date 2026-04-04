# Arkhé Finance API

API REST de controle financeiro pessoal desenvolvida em Python com FastAPI e SQLite.

Esse é meu terceiro projeto pessoal, desenvolvido no primeiro semestre de Ciência da Computação com foco em aprender desenvolvimento backend.

---

## Tech Stack

- Python
- FastAPI
- SQLite
- Uvicorn

---

## Como rodar
```bash
cat > README.md << 'EOF'
# Arkhé Finance API

API REST de controle financeiro pessoal desenvolvida em Python com FastAPI e SQLite.

Esse é meu terceiro projeto pessoal, desenvolvido no primeiro semestre de Ciência da Computação com foco em aprender desenvolvimento backend.

---

## Tech Stack

- Python
- FastAPI
- SQLite
- Uvicorn

---

## Como rodar
```bash
git clone https://github.com/Thiago-Mateus0/arkhe-finance-api
cd arkhe-finance-api
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
python -m uvicorn main:app --reload
```

Acesse a documentação em: http://localhost:8000/docs

---

## Endpoints

### Transações

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | /transacoes | Lista todas as transações |
| GET | /transacoes?tipo=saida | Filtra por tipo |
| POST | /transacoes | Cria uma transação |
| PUT | /transacoes/{id} | Atualiza uma transação |
| DELETE | /transacoes/{id} | Deleta uma transação |

### Categorias

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | /categorias | Lista todas as categorias |
| POST | /categorias | Cria uma categoria |
| DELETE | /categorias/{id} | Deleta uma categoria |

### Dashboard

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | /dashboard | Saldo, entradas, saídas e gastos por categoria |

---

## Sobre

Feito por [Thiago Mateus](https://github.com/Thiago-Mateus0) — calouro de Ciência da Computação aprendendo backend na prática.
