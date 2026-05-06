import sqlite3

DB_NAME = "f1.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS drivers (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre       TEXT    NOT NULL,
            equipo       TEXT    NOT NULL,
            nacionalidad TEXT    NOT NULL,
            numero       INTEGER NOT NULL,
            imagen       TEXT
        )
    """)
    conn.commit()
    conn.close()