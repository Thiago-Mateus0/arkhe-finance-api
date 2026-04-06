Arkhé Finance API

API REST para controle financeiro pessoal, desenvolvida com Python, FastAPI e SQLite.

Permite gerenciar transações (entradas e saídas), categorias e visualizar um resumo financeiro consolidado.

Visão geral

A API foi projetada para centralizar o controle financeiro, oferecendo:

Registro de transações (entrada e saída)
Organização por categorias
Filtros por tipo, data e categoria
Cálculo automático de saldo e resumo financeiro
Tecnologias
Python 3
FastAPI
SQLite
Uvicorn
Funcionalidades
Transações
Criar transações
Listar transações
Atualizar transações
Deletar transações
Filtrar por tipo (entrada / saída)
Filtrar por categoria
Filtrar por intervalo de datas
Categorias
Criar categorias
Listar categorias
Deletar categorias
Dashboard
Total de entradas
Total de saídas
Saldo atual
Distribuição por categoria
Estrutura do projeto
.
├── app
│   ├── database.py
│   └── routes
│       ├── categorias.py
│       ├── dashboard.py
│       └── transacoes.py
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
Método	Rota	Descrição
GET	/transacoes	Lista todas
GET	/transacoes?tipo=entrada	Filtra por tipo
GET	/transacoes?categoria_id=1	Filtra por categoria
GET	/transacoes?data_inicio=YYYY-MM-DD&data_fim=YYYY-MM-DD	Filtra por período
POST	/transacoes	Cria nova
PUT	/transacoes/{id}	Atualiza
DELETE	/transacoes/{id}	Remove
Categorias
Método	Rota	Descrição
GET	/categorias	Lista todas
POST	/categorias	Cria nova
DELETE	/categorias/{id}	Remove
Dashboard
Método	Rota	Descrição
GET	/dashboard	Retorna resumo financeiro
Exemplos
Criar categoria
{
  "nome": "Alimentação",
  "tipo": "saida"
}
Criar transação
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
Autenticação com JWT
Paginação de resultados
Testes automatizados
Deploy da API
Validações com Pydantic
Autor

Thiago Mateus
Estudante de Ciência da Computação com foco em desenvolvimento backend

Be water, my friend.
