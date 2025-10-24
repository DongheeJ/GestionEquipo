import tkinter as tk
from tkinter import ttk

class Prestamo_view:
    def __init__(self, root):
        self.root = root
        self.root.title("Préstamo de equipo")
        self.root.geometry("700x500")  # 창 크기: 가로 300, 세로 200

        # 전체를 2열 구조로 만들기
        root.columnconfigure(0, weight=1)  # 왼쪽 열 (입력란)
        root.columnconfigure(1, weight=1)  # 오른쪽 열 (버튼들)

        # ─────────────── 왼쪽 영역 ───────────────
        frame_inputs = tk.Frame(root)
        frame_inputs.grid(row=0, column=0, padx=30, pady=20, sticky="nw")

        # Estudiante
        frame_ipEstudiante = tk.Frame(frame_inputs)
        frame_ipEstudiante.pack(pady=5, anchor="w")
        tk.Label(frame_ipEstudiante, text="Estudiante:").grid(row=0, column=0, padx=5)
        self.inputEstudiante = tk.Entry(frame_ipEstudiante, width=25)
        self.inputEstudiante.grid(row=0, column=1, padx=5)

        # Placa
        frame_ipPlaca = tk.Frame(frame_inputs)
        frame_ipPlaca.pack(pady=5, anchor="w")
        tk.Label(frame_ipPlaca, text="Placa:").grid(row=0, column=0, padx=5)
        self.inputPlaca = tk.Entry(frame_ipPlaca, width=25)
        self.inputPlaca.grid(row=0, column=1, padx=5)

        # Multa
        frame_ipMulta = tk.Frame(frame_inputs)
        frame_ipMulta.pack(pady=5, anchor="w")
        tk.Label(frame_ipMulta, text="Multa:").grid(row=0, column=0, padx=5)
        self.inputMulta = tk.Entry(frame_ipMulta, width=25)
        self.inputMulta.grid(row=0, column=1, padx=5)

        # Hora inicio / final (여기! 변수 유지)
        self.hora_inicio_var = tk.StringVar(value="")
        self.hora_final_var  = tk.StringVar(value="")

        f_hi = tk.Frame(frame_inputs)
        f_hi.pack(anchor="w", pady=5)
        tk.Label(f_hi, text="Hora inicio:").grid(row=0, column=0, padx=5, sticky="w")
        tk.Label(f_hi, textvariable=self.hora_inicio_var).grid(row=0, column=1, padx=5, sticky="w")

        f_hf = tk.Frame(frame_inputs)
        f_hf.pack(anchor="w", pady=5)
        tk.Label(f_hf, text="Hora final:").grid(row=0, column=0, padx=5, sticky="w")
        tk.Label(f_hf, textvariable=self.hora_final_var).grid(row=0, column=1, padx=5, sticky="w")

        # Consumibles
        self.frame_ipConsumibles = tk.Frame(frame_inputs)
        self.frame_ipConsumibles.pack(pady=10, anchor="w")
        self.consumibles = []

        # ─────────────── 오른쪽 영역 ───────────────
        frame_botones = tk.Frame(root)
        frame_botones.grid(row=0, column=1, padx=20, pady=20, sticky="ne")

        btn_add = tk.Button(frame_botones, text="➕", command=self.add_consumible, width=12)
        btn_add.grid(row=0, column=0, padx=5, pady=5)

        btn_show = tk.Button(frame_botones, text="Mostrar", command=self.show_values, width=12)
        btn_show.grid(row=0, column=1, padx=5, pady=5)

        self.btn_registrar = tk.Button(frame_botones, text="Registrar", width=12)
        self.btn_registrar.grid(row=0, column=2, padx=5, pady=5)

        self.btn_consultar = tk.Button(frame_botones, text="Consultar", width=12)
        self.btn_consultar.grid(row=1, column=0, padx=5, pady=5)

        self.btn_entregar = tk.Button(frame_botones, text="Entregar", width=12)
        self.btn_entregar.grid(row=1, column=1, padx=5, pady=5)

        self.btn_clear = tk.Button(frame_botones, text="Limpiar datos", width=12)
        self.btn_clear.grid(row=1, column=2, padx=5, pady=5)

    def get_placa(self):
        return self.inputPlaca.get()
    def get_inf_Estudiante(self):
        return self.inputEstudiante.get()
    def get_multa(self):
        return self.inputMulta.get()
    def get_consumibles(self):
        consumibles = []
        for c in self.consumibles:
            consumibles.append(c.get())
        return consumibles
    
    def set_placa(self,placa):
        self.inputPlaca.delete(0, tk.END)
        self.inputPlaca.insert(0,placa)
    def set_hora_inicio(self, hora_inicio):
        self.hora_inicio_var.set(hora_inicio)
    def set_hora_final(self, hora_final):
        self.hora_final_var.set(hora_final)

    def clear(self):
        self.inputEstudiante.delete(0,tk.END)
        self.inputPlaca.delete(0,tk.END)
        self.inputMulta.delete(0,tk.END)
        self.hora_inicio_var.set("")
        self.clear_consumibles()

    def add_consumible(self):
        var = tk.StringVar()
        entry = tk.Entry(self.frame_ipConsumibles, width=30, textvariable=var)
        entry.pack(pady=3, anchor="w")
        self.consumibles.append(var)

    def clear_consumibles(self):
        for c in self.consumibles:
            c.set("")

    def show_values(self):
        """모든 Entry 내용 출력"""
        for i, e in enumerate(self.consumibles, start=1):
            print(f"Consumible {i}: {e.get()}")
