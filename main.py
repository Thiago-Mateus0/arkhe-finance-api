from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database import init_db
from app.routes import transacoes
from app.routes import categorias
from app.routes import dashboard

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(dashboard.router)

app.include_router(categorias.router)
app.include_router(transacoes.router)

@app.get("/")
def root():
    return {"mensagem": "Arkhé Finance API funcionando!"}

