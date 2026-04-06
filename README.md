diff --git a/README.md b/README.md
index 8e54881c4c6da2a6e82f7c9c7ed5bb9bc0c25fa9..6e445efc64893fb3624787f70e693bd8d51b29dd 100644
--- a/README.md
+++ b/README.md
@@ -1,79 +1,121 @@
 # Arkhé Finance API
 
-API REST de controle financeiro pessoal desenvolvida em Python com FastAPI e SQLite.
-
-Esse é meu terceiro projeto pessoal, desenvolvido no primeiro semestre de Ciência da Computação com foco em aprender desenvolvimento backend.
-
----
-
-## Tech Stack
-
-- Python
-- FastAPI
-- SQLite
-- Uvicorn
+API REST para controle financeiro pessoal, construída com **FastAPI** e **SQLite**.
 
 ---
 
-## Como rodar
-```bash
-cat > README.md << 'EOF'
-# Arkhé Finance API
+## ✨ Funcionalidades
 
-API REST de controle financeiro pessoal desenvolvida em Python com FastAPI e SQLite.
-
-Esse é meu terceiro projeto pessoal, desenvolvido no primeiro semestre de Ciência da Computação com foco em aprender desenvolvimento backend.
+- Cadastro, listagem, atualização e remoção de transações.
+- Cadastro, listagem e remoção de categorias.
+- Dashboard com:
+  - total de entradas
+  - total de saídas
+  - saldo atual
+  - gastos por categoria
+- Filtros de transações por tipo, categoria e intervalo de datas.
 
 ---
 
-## Tech Stack
+## 🧱 Tecnologias
 
-- Python
+- Python 3.10+
 - FastAPI
-- SQLite
 - Uvicorn
+- SQLite
 
 ---
 
-## Como rodar
+## 🚀 Como executar localmente
+
 ```bash
 git clone https://github.com/Thiago-Mateus0/arkhe-finance-api
 cd arkhe-finance-api
 python3 -m venv venv
 source venv/bin/activate
 pip install fastapi uvicorn
-python -m uvicorn main:app --reload
+uvicorn main:app --reload
 ```
 
-Acesse a documentação em: http://localhost:8000/docs
+A API estará disponível em:
+
+- App: `http://127.0.0.1:8000`
+- Swagger UI: `http://127.0.0.1:8000/docs`
+- ReDoc: `http://127.0.0.1:8000/redoc`
 
 ---
 
-## Endpoints
+## 🧭 Endpoints
 
 ### Transações
+
 | Método | Rota | Descrição |
-|--------|------|-----------|
-| GET | /transacoes | Lista todas as transações |
-| GET | /transacoes?tipo=saida | Filtra por tipo |
-| POST | /transacoes | Cria uma transação |
-| PUT | /transacoes/{id} | Atualiza uma transação |
-| DELETE | /transacoes/{id} | Deleta uma transação |
+|---|---|---|
+| GET | `/transacoes` | Lista todas as transações |
+| GET | `/transacoes?tipo=saida` | Filtra por tipo |
+| GET | `/transacoes?categoria_id=1` | Filtra por categoria |
+| GET | `/transacoes?data_inicio=2026-01-01&data_fim=2026-01-31` | Filtra por período |
+| POST | `/transacoes` | Cria uma transação |
+| PUT | `/transacoes/{id}` | Atualiza uma transação |
+| DELETE | `/transacoes/{id}` | Remove uma transação |
 
 ### Categorias
+
 | Método | Rota | Descrição |
-|--------|------|-----------|
-| GET | /categorias | Lista todas as categorias |
-| POST | /categorias | Cria uma categoria |
-| DELETE | /categorias/{id} | Deleta uma categoria |
+|---|---|---|
+| GET | `/categorias` | Lista categorias |
+| POST | `/categorias` | Cria categoria |
+| DELETE | `/categorias/{id}` | Remove categoria |
 
 ### Dashboard
+
 | Método | Rota | Descrição |
-|--------|------|-----------|
-| GET | /dashboard | Saldo, entradas, saídas e gastos por categoria |
+|---|---|---|
+| GET | `/dashboard` | Retorna resumo financeiro |
+
+---
+
+## 🧪 Exemplos de payload
+
+### Criar categoria
+
+```json
+{
+  "nome": "Mercado",
+  "tipo": "saida"
+}
+```
+
+### Criar transação
+
+```json
+{
+  "tipo": "saida",
+  "valor": 89.9,
+  "descricao": "Compras da semana",
+  "categoria_id": 1,
+  "data": "2026-04-06"
+}
+```
+
+---
+
+## 📁 Estrutura do projeto
+
+```text
+.
+├── main.py
+├── app
+│   ├── database.py
+│   └── routes
+│       ├── categorias.py
+│       ├── dashboard.py
+│       └── transacoes.py
+└── README.md
+```
 
 ---
 
-## Sobre
+## 👤 Autor
 
-Feito por [Thiago Mateus](https://github.com/Thiago-Mateus0) — calouro de Ciência da Computação aprendendo backend na prática.
+Feito por [Thiago Mateus](https://github.com/Thiago-Mateus0).
