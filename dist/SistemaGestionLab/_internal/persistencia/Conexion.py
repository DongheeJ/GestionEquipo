import sqlite3
import os
import sys
from pathlib import Path

def get_conn() -> sqlite3.Connection:
    # 1. 실행 환경에 따른 루트 경로 결정
    if getattr(sys, 'frozen', False):
        # EXE로 실행 중일 때: EXE 파일이 있는 폴더
        base_path = Path(sys.executable).parent
    else:
        # .py 소스 코드로 실행 중일 때: 현재 파일의 조상 폴더 (root)
        base_path = Path(__file__).resolve().parent.parent

    # 2. DB 경로 설정 (프로젝트 루트의 GestionEquipo.db)
    db_path = base_path / "GestionEquipo.db"

    # 3. 연결 생성
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")
    return conn