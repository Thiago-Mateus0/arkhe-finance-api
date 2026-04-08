API REST de controle financeiro pessoal — desenvolvida do zero por um estudante de Ciência da Computação.🚀 Deploy e AcessoA API está em produção e pode ser acessada publicamente.AmbienteURLAPI (Produção)https://arkhe-finance-api.onrender.comDocumentação (Swagger)https://arkhe-finance-api.onrender.com/docsSobre o projetoO Arkhé Finance API centraliza o controle financeiro pessoal via HTTP. Permite registrar entradas e saídas, organizar por categorias, filtrar transações e visualizar um resumo financeiro consolidado.Desenvolvido como projeto de portfólio durante o primeiro semestre de Ciência da Computação, com foco em fundamentos reais de backend e arquitetura de APIs.TecnologiasFerramentaUsoPython 3Linguagem principalFastAPIFramework da APISQLiteBanco de dados (Persistência local)UvicornServidor ASGIRenderPlataforma de Hospedagem (PaaS)Como executar localmenteBash# Clonar o repositório
git clone https://github.com/Thiago-Mateus0/arkhe-finance-api
cd arkhe-finance-api

# Configurar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependências
pip install fastapi uvicorn

# Executar a API
python -m uvicorn main:app --reload
EndpointsTransaçõesMétodoRotaDescriçãoGET/transacoesLista todasGET/transacoes?tipo=entradaFiltra por tipoGET/transacoes?categoria_id=1Filtra por categoriaGET/transacoes?data_inicio=YYYY-MM-DD&data_fim=YYYY-MM-DDFiltra por períodoPOST/transacoesCria novaPUT/transacoes/{id}AtualizaDELETE/transacoes/{id}RemoveCategorias e DashboardMétodoRotaDescriçãoGET/categoriasLista todasPOST/categoriasCria novaGET/dashboardResumo financeiro consolidadoExemplos de JSONCriar transação (POST /transacoes)JSON{
  "tipo": "saida",
  "valor": 120.50,
  "descricao": "Supermercado",
  "categoria_id": 1,
  "data": "2026-04-06"
}
Resposta do dashboardJSON{
  "entradas": 3000.00,
  "saidas": 850.00,
  "saldo": 2150.00,
  "gastos_por_categoria": [
    { "nome": "Alimentação", "total": 450.00 },
    { "nome": "Transporte", "total": 400.00 }
  ]
}
Estrutura do projetoPlaintextarkhe-finance-api/
├── app/
│   ├── database.py
│   └── routes/
│       ├── transacoes.py
│       ├── categorias.py
│       └── dashboard.py
├── main.py
├── .gitignore
└── README.md
Melhorias futuras[x] Deploy da API (Render)[ ] Migração para banco de dados PostgreSQL[ ] Autenticação com JWT[ ] Paginação de resultados[ ] Testes automatizados com Pytest[ ] Validações avançadas com PydanticAutorThiago Mateus — estudante de Ciência da Computação com foco em desenvolvimento backend."Be water, my friend." — Bruce Lee
