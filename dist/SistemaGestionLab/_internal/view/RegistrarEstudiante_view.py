# view/Estudiante_form_view.py
import tkinter as tk
from tkinter import ttk

class RegistrarEstudiante_view:
    def __init__(self, root):
        self.root = root
        width, height = 400, 300
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.root.title("Registrar estudiante")

        frame = tk.Frame(root, padx=10, pady=10)
        frame.pack(fill="both", expand=True)

        # ===== StringVars =====
        self.nombre_var = tk.StringVar()
        self.apellido_var = tk.StringVar()
        self.correo_var = tk.StringVar()
        self.celular_var = tk.StringVar()
        self.codigo_var = tk.StringVar()
        self.cedula_var = tk.StringVar()
        self.proyecto_var = tk.StringVar()

        # ===== Campos =====
        tk.Label(frame, text="Nombre:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(frame, textvariable=self.nombre_var, width=30).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Apellido:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(frame, textvariable=self.apellido_var, width=30).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Correo:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(frame, textvariable=self.correo_var, width=30).grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame, text="Celular:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(frame, textvariable=self.celular_var, width=30).grid(row=3, column=1, padx=5, pady=5)

        tk.Label(frame, text="Código:").grid(row=4, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(frame, textvariable=self.codigo_var, width=30).grid(row=4, column=1, padx=5, pady=5)

        tk.Label(frame, text="Cédula:").grid(row=5, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(frame, textvariable=self.cedula_var, width=30).grid(row=5, column=1, padx=5, pady=5)

        tk.Label(frame, text="Proyecto curricular:").grid(row=6, column=0, sticky="e", padx=5, pady=5)
        self.combo_proyecto = ttk.Combobox(frame, textvariable=self.proyecto_var, state="normal", width=28)
        self.combo_proyecto.grid(row=6, column=1, padx=5, pady=5)

        self.proyectos_nombres = []          # 전체 목록 저장용
        self._proyecto_filter_after_id = None
        
        self.combo_proyecto.bind("<KeyRelease>", self._filtrar_proyectos_debounced)

        # ===== Botones =====
        btn_frame = tk.Frame(frame)
        btn_frame.grid(row=7, column=0, columnspan=2, pady=10)

        self.btn_guardar = tk.Button(btn_frame, text="Guardar")
        self.btn_guardar.grid(row=0, column=0, padx=5)

        self.btn_cancelar = tk.Button(btn_frame, text="Cancelar")
        self.btn_cancelar.grid(row=0, column=1, padx=5)

    # ---- 프로젝트 목록 세팅 ----
    def set_proyectos(self, nombres_proyectos):
        """컨트롤러에서 프로젝트 목록 세팅할 때 호출"""
        self.proyectos_nombres = nombres_proyectos[:]  # 전체 목록 보관
        self.combo_proyecto["values"] = nombres_proyectos

    def _filtrar_proyectos_debounced(self, event=None):
        texto = self.combo_proyecto.get().lower()

        # 이전 after 예약 취소
        if self._proyecto_filter_after_id is not None:
            self.root.after_cancel(self._proyecto_filter_after_id)

        # 150ms 뒤에 실제 필터 실행 (디바운스)
        self._proyecto_filter_after_id = self.root.after(
            150,
            lambda: self._aplicar_filtro_proyectos(texto)
        )

    def _aplicar_filtro_proyectos(self, texto):
        if not texto:
            filtrados = self.proyectos_nombres
        else:
            filtrados = [
                nombre for nombre in self.proyectos_nombres
                if texto in nombre.lower()
            ]

        self.combo_proyecto["values"] = filtrados

    # ---- 핸들러 연결 ----
    def set_guardar_handler(self, handler):
        self.btn_guardar.config(command=handler)

    def set_cancelar_handler(self, handler):
        self.btn_cancelar.config(command=handler)

    # ---- 폼 데이터 꺼내기 ----
    def get_datos(self):
        return {
            "nombre": self.nombre_var.get().strip(),
            "apellido": self.apellido_var.get().strip(),
            "correo": self.correo_var.get().strip(),
            "celular": self.celular_var.get().strip(),
            "codigo": self.codigo_var.get().strip(),
            "cedula": self.cedula_var.get().strip(),
            "proyecto_nombre": self.proyecto_var.get().strip(),
        }
