import sqlite3

DB_PATH = "financas.db"

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn
def init_db():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            tipo TEXT NOT NULL CHECK(tipo IN ('entrada', 'saida', 'ambos'))
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL CHECK(tipo IN ('entrada', 'saida')),
            valor REAL NOT NULL CHECK(valor > 0),
            descricao TEXT NOT NULL,
            categoria_id INTEGER NOT NULL REFERENCES categorias(id),
            data TEXT NOT NULL
        )
    """)

    total = cursor.execute("SELECT COUNT(*) FROM categorias").fetchone()[0]

    if total == 0:
        categorias_padrao = [
            ("Salário", "entrada"),
            ("Freelancer", "entrada"),
            ("Comissão", "entrada"),
            ("Bônus", "entrada"),
            ("Hora extra", "entrada"),
            ("Energia", "saida"),
            ("Água", "saida"),
            ("Internet", "saida"),
            ("Mercado", "saida"),
            ("Restaurante", "saida"),
            ("Delivery", "saida"),
            ("Lanche / Padaria", "saida"),
            ("Uber / 99", "saida"),
            ("Transporte público", "saida"),
            ("Combustível", "saida"),
            ("Estacionamento", "saida"),
            ("Faculdade", "saida"),
            ("Curso online", "saida"),
            ("Netflix / Spotify / Prime", "saida"),
            ("Farmácia", "saida"),
            ("Academia", "saida"),
            ("Recarga", "saida"),
            ("Fatura do cartão", "saida"),
            ("Outros", "ambos"),
        ]

        cursor.executemany(
            "INSERT INTO categorias (nome, tipo) VALUES (?, ?)",
            categorias_padrao
        )

    conn.commit()
    conn.close()