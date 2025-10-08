import tkinter as tk
from tkinter import ttk

class Prestamo_view:
    def __init__(self, root):
        self.root = root
        self.root.title("Préstamo de equipo")
        self.root.geometry("700x500")  # 창 크기: 가로 300, 세로 200

        frame_ipEstudiante = tk.Frame(root)
        frame_ipEstudiante.pack(pady=10)
        tk.Label(frame_ipEstudiante, text="Estudiante:").grid(row=0, column=0, padx=5)
        self.inputEstudiante = tk.Entry(frame_ipEstudiante)
        self.inputEstudiante.grid(row=0, column=1, padx=5)
        
        frame_ipPlaca = tk.Frame(root)
        frame_ipPlaca.pack(pady=10)
        tk.Label(frame_ipPlaca, text="Placa:").grid(row=0, column=0, padx=5)
        self.inputPlaca= tk.Entry(frame_ipPlaca)
        self.inputPlaca.grid(row=0, column=1, padx=5)
        
        frame_ipMulta = tk.Frame(root)
        frame_ipMulta.pack(pady=10)
        tk.Label(frame_ipMulta, text="Multa:").grid(row=0, column=0, padx=5)
        self.inputMulta= tk.Entry(frame_ipMulta)
        self.inputMulta.grid(row=0, column=1, padx=5)
        
        hora_inicio = tk.StringVar()
        hora_inicio.set("2025-10-10")  # 초기값 설정
        label = tk.Label(root, textvariable=hora_inicio)
        label.pack(pady=5)
        entry = tk.Entry(root, textvariable=hora_inicio)
        entry.pack(pady=5)

        self.frame_ipConsumibles = tk.Frame(root)
        self.frame_ipConsumibles.pack(pady=10)
        self.consumibles = []

        btn_add = tk.Button(root, text="➕", command=self.add_consumible)
        btn_add.pack(pady=5)

        btn_show = tk.Button(root, text="Mostrar", command=self.show_values)
        btn_show.pack(pady=5)

    def add_consumible(self):
        """새 Entry 추가"""
        entry = tk.Entry(self.frame_ipConsumibles, width=30)
        entry.pack(pady=3)
        self.consumibles.append(entry)
    
    def show_values(self):
        """모든 Entry 내용 출력"""
        for i, e in enumerate(self.consumibles, start=1):
            print(f"Consumible {i}: {e.get()}")
