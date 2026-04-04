from fastapi import APIRouter
from pydantic import BaseModel
from app.database import get_db

router = APIRouter()

class CategoriaInput(BaseModel):
    nome: str
    tipo: str

@router.get("/categorias")
def listar_categorias():
    conn = get_db()
    cursor = conn.cursor()

    categorias = cursor.execute(
        "SELECT id, nome, tipo FROM categorias ORDER BY tipo, nome"
    ).fetchall()

    conn.close()

    return [dict(c) for c in categorias]

@router.post("/categorias")
def criar_categoria(categoria: CategoriaInput):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO categorias (nome, tipo) VALUES (?, ?)",
        (categoria.nome, categoria.tipo)
    )

    conn.commit()
    conn.close()

    return {"mensagem": "Categoria criada com sucesso!"}

@router.delete("/categorias/{id}")
def deletar_categoria(id: int):
    conn = get_db()
    cursor = conn.cursor()

    row = cursor.execute("SELECT id FROM categorias WHERE id = ?", (id,)).fetchone()

    if row is None:
        conn.close()
        return {"erro": "Categoria não encontrada"}

    cursor.execute("DELETE FROM categorias WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return {"mensagem": "Categoria deletada com sucesso!"}