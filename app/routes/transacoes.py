from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.database import get_db


router = APIRouter()


class TransacaoInput(BaseModel):
    tipo: str
    valor: float
    descricao: str
    categoria_id: int
    data: str


@router.get("/transacoes")
def listar_transacoes(
    tipo: Optional[str] = None,
    categoria_id: Optional[int] = None,
    data_inicio: Optional[str] = None,
    data_fim: Optional[str] = None
):
    conn = get_db()
    cursor = conn.cursor()

    query = """
        SELECT t.id, t.tipo, t.valor, t.descricao, t.data, c.nome as categoria
        FROM transacoes t
        JOIN categorias c ON c.id = t.categoria_id
        WHERE 1=1
    """
    params = []

    if tipo:
        query += " AND t.tipo = ?"
        params.append(tipo)

    if categoria_id:
        query += " AND t.categoria_id = ?"
        params.append(categoria_id)

    if data_inicio:
        query += " AND t.data >= ?"
        params.append(data_inicio)

    if data_fim:
        query += " AND t.data <= ?"
        params.append(data_fim)

    query += " ORDER BY t.data DESC"

    transacoes = cursor.execute(query, params).fetchall()
    conn.close()

    return [dict(t) for t in transacoes]


@router.post("/transacoes")
def criar_transacao(transacao: TransacaoInput):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO transacoes (tipo, valor, descricao, categoria_id, data)
        VALUES (?, ?, ?, ?, ?)
    """, (transacao.tipo, transacao.valor, transacao.descricao, transacao.categoria_id, transacao.data))
    conn.commit()
    conn.close()
    return {"mensagem": "Transação criada com sucesso!"}


@router.delete("/transacoes/{id}")
def deletar_transacao(id: int):
    conn = get_db()
    cursor = conn.cursor()

    row = cursor.execute("SELECT id FROM transacoes WHERE id = ?", (id,)).fetchone()

    if row is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Não encontrado")

    cursor.execute("DELETE FROM transacoes WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return {"mensagem": "Transação deletada com sucesso!"}


@router.put("/transacoes/{id}")
def atualizar_transacao(id: int, transacao: TransacaoInput):
    conn = get_db()
    cursor = conn.cursor()

    row = cursor.execute("SELECT id FROM transacoes WHERE id = ?", (id,)).fetchone()

    if row is None:
        conn.close()
        return {"erro": "Transação não encontrada"}

    cursor.execute("""
        UPDATE transacoes
        SET tipo = ?, valor = ?, descricao = ?, categoria_id = ?, data = ?
        WHERE id = ?
    """, (transacao.tipo, transacao.valor, transacao.descricao, transacao.categoria_id, transacao.data, id))

    conn.commit()
    conn.close()

    return {"mensagem": "Transação atualizada com sucesso!"}