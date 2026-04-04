from fastapi import APIRouter
from app.database import get_db

router = APIRouter()

@router.get("/dashboard")
def dashboard():
    conn = get_db()
    cursor = conn.cursor()

    entradas = cursor.execute(
        "SELECT SUM(valor) FROM transacoes WHERE tipo = 'entrada'"
    ).fetchone()[0] or 0

    saidas = cursor.execute(
        "SELECT SUM(valor) FROM transacoes WHERE tipo = 'saida'"
    ).fetchone()[0] or 0

    gastos_por_categoria = cursor.execute("""
        SELECT c.nome, SUM(t.valor) as total
        FROM transacoes t
        JOIN categorias c ON c.id = t.categoria_id
        WHERE t.tipo = 'saida'
        GROUP BY c.nome
        ORDER BY total DESC
    """).fetchall()

    conn.close()

    return {
        "entradas": entradas,
        "saidas": saidas,
        "saldo": entradas - saidas,
        "gastos_por_categoria": [dict(g) for g in gastos_por_categoria]
    }
    