Arkhé Finance API

API REST para controle financeiro pessoal, desenvolvida com Python, FastAPI e SQLite.

O projeto permite gerenciar entradas e saídas financeiras, categorias e visualizar um resumo consolidado dos dados.

Visão geral

A API foi projetada para centralizar o controle de finanças pessoais, oferecendo:

registro de transações (entradas e saídas)
organização por categorias
filtros por tipo, data e categoria
cálculo automático de saldo e resumo financeiro
Tecnologias
Python 3
FastAPI
SQLite
Uvicorn
Funcionalidades
Transações
criar transações
listar transações
atualizar transações
deletar transações
filtrar por tipo (entrada / saida)
filtrar por categoria
filtrar por intervalo de datas
Categorias
criar categorias
listar categorias
deletar categorias
Dashboard
total de entradas
total de saídas
saldo atual
distribuição por categoria
Estrutura do projeto

.
├── app
│ ├── database.py
│ └── routes
│ ├── categorias.py
│ ├── dashboard.py
│ └── transacoes.py
├── main.py
├── .gitignore
└── README.md

Como executar

git clone https://github.com/Thiago-Mateus0/arkhe-finance-api

cd arkhe-finance-api

python3 -m venv venv
source venv/bin/activate

pip install fastapi uvicorn
uvicorn main:app --reload

A API estará disponível em:

http://127.0.0.1:8000

http://127.0.0.1:8000/docs

Endpoints
Transações

GET /transacoes → Lista todas
GET /transacoes?tipo=entrada → Filtra por tipo
GET /transacoes?categoria_id=1 → Filtra por categoria
GET /transacoes?data_inicio=YYYY-MM-DD&data_fim=YYYY-MM-DD → Filtra por período
POST /transacoes → Cria nova
PUT /transacoes/{id} → Atualiza
DELETE /transacoes/{id} → Remove

Categorias

GET /categorias → Lista todas
POST /categorias → Cria nova
DELETE /categorias/{id} → Remove

Dashboard

GET /dashboard → Retorna resumo financeiro

Exemplos

Criar categoria:

{
"nome": "Alimentação",
"tipo": "saida"
}

Criar transação:

{
"tipo": "saida",
"valor": 120.50,
"descricao": "Supermercado",
"categoria_id": 1,
"data": "2026-04-06"
}

Resposta inicial

{
"mensagem": "Arkhé Finance API funcionando!"
}

Melhorias futuras
autenticação com JWT
paginação de resultados
testes automatizados
deploy da API
validações mais robustas com Pydantic
Autor

Thiago Mateus
Estudante de Ciência da Computação com foco em desenvolvimento backend

Projeto desenvolvido como parte da evolução prática em construção de APIs.

Be water, my friend.
