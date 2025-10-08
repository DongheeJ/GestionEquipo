import sqlite3
from pathlib import Path

def get_conn() -> sqlite3.Connection:
    base = Path(__file__).resolve().parent
    db = (base.parent / "GestionEquipo.db")
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    return conn