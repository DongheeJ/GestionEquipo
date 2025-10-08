import tkinter as tk
from tkinter import ttk

class Equipo_view:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Equipos")

        # 상단 입력 프레임
        frame_form = tk.Frame(root)
        frame_form.pack(pady=10)

        tk.Label(frame_form, text="Placa:").grid(row=0, column=0, padx=5)
        self.entry_placa = tk.Entry(frame_form)
        self.entry_placa.grid(row=0, column=1, padx=5)

        # 버튼 프레임
        frame_btn = tk.Frame(root)
        frame_btn.pack(pady=10)

        self.btn_listar = tk.Button(frame_btn, text="Listar equipos")
        self.btn_listar.grid(row=0, column=0, padx=5)

        self.btn_guardar = tk.Button(frame_btn, text="Guardar equipo")
        self.btn_guardar.grid(row=0, column=1, padx=5)

        # 테이블 (Treeview)
        self.tabla = ttk.Treeview(root, columns=("ID", "Placa"), show="headings")
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Placa", text="Placa")
        self.tabla.pack(pady=10)

    # 📦 Controller에서 데이터 받아서 테이블 표시
    def mostrar_tabla(self, datos):
        # 기존 데이터 삭제
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        # 새 데이터 추가
        for d in datos:
            self.tabla.insert("", "end", values=d)

    # 📝 입력값 가져오기
    def get_placa(self):
        return self.entry_placa.get()