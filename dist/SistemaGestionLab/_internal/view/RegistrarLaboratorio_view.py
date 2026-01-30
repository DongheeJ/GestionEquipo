import tkinter as tk
from tkinter import ttk, messagebox

class RegistrarLaboratorio_view:
    def __init__(self, root):
        self.root = root
        width, height = 300, 300
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.root.title("Registrar Laboratorio")

        # ====== 상단 입력 프레임 ======
        frame_form = tk.Frame(root)
        frame_form.pack(padx=20, pady=30)

        # Placa
        tk.Label(frame_form, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_nombre = tk.Entry(frame_form, width=25)
        self.entry_nombre.grid(row=0, column=1, padx=5, pady=5)

        # ====== 버튼 프레임 ======
        frame_btn = tk.Frame(root)
        frame_btn.pack(pady=20)

        # 컨트롤러에서 command를 연결해줄 버튼
        self.btn_registrar = tk.Button(frame_btn, text="Registrar")
        self.btn_registrar.grid(row=0, column=0, padx=10)

        self.btn_cancelar = tk.Button(frame_btn, text="Cancelar", command=root.destroy)
        self.btn_cancelar.grid(row=0, column=1, padx=10)

    # ---------- getter들 (컨트롤러에서 insert 할 때 사용) ----------
    def get_nombre(self):
        return self.entry_nombre.get().strip()

    # ---------- 메시지 도우미 ----------
    def mostrar_mensaje(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)

    def mostrar_error(self, titulo, mensaje):
        messagebox.showerror(titulo, mensaje)

    def confirmar(self, titulo, mensaje):
        return messagebox.askyesno(titulo, mensaje)