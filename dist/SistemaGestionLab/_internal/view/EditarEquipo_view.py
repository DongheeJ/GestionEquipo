# view/Estudiante_form_view.py
import tkinter as tk
from tkinter import ttk

class EditarEquipo_view:
    def __init__(self, root):
        self.root = root
        width, height = 300, 300
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.root.title("Editar equipo")

        frame = tk.Frame(root, padx=10, pady=10)
        frame.pack(fill="both", expand=True)

        # ===== StringVars =====
        self.placa_var = tk.StringVar()
        self.elemento_var = tk.StringVar()
        self.laboratorio_var = tk.StringVar()

        # ===== Campos =====
        tk.Label(frame, text="placa:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(frame, textvariable=self.placa_var, width=30).grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="elemento:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.combo_elemento = ttk.Combobox(frame, textvariable=self.elemento_var, state="normal", width=28)
        self.combo_elemento.grid(row=1, column=1, padx=5, pady=5)

        self.elementos_nombres = []          # 전체 목록 저장용
        self._elemento_filter_after_id = None
        
        self.combo_elemento.bind("<KeyRelease>", self._filtrar_elementos_debounced)

        tk.Label(frame, text="laboratorio:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.combo_laboratorio = ttk.Combobox(frame, textvariable=self.laboratorio_var, state="normal", width=28)
        self.combo_laboratorio.grid(row=2, column=1, padx=5, pady=5)

        self.laboratorios_nombres = []          # 전체 목록 저장용
        self._laboratorio_filter_after_id = None
        
        self.combo_laboratorio.bind("<KeyRelease>", self._filtrar_laboratorios_debounced)

        # ===== Botones =====
        btn_frame = tk.Frame(frame)
        btn_frame.grid(row=7, column=0, columnspan=2, pady=10)

        self.btn_editar = tk.Button(btn_frame, text="Guardar cambios")
        self.btn_editar.grid(row=0, column=0, padx=5)

        self.btn_cancelar = tk.Button(btn_frame, text="Cancelar")
        self.btn_cancelar.grid(row=0, column=1, padx=5)

    def set_elementos(self, nombres_elementos):
        self.elementos_nombres = nombres_elementos[:]  # 전체 목록 보관
        self.combo_elemento["values"] = nombres_elementos

    def set_laboratorios(self, nombres_laboratorios):
        self.laboratorios_nombres = nombres_laboratorios[:]  # 전체 목록 보관
        self.combo_laboratorio["values"] = nombres_laboratorios

    def _filtrar_elementos_debounced(self, event=None):
        texto = self.combo_elemento.get()

        # 이전 after 예약 취소
        if self._elemento_filter_after_id is not None:
            self.root.after_cancel(self._elemento_filter_after_id)

        # 150ms 뒤에 실제 필터 실행 (디바운스)
        self._elemento_filter_after_id = self.root.after(
            150,
            lambda: self._aplicar_filtro_elementos(texto)
        )

    def _filtrar_laboratorios_debounced(self, event=None):
        texto = self.combo_laboratorio.get()

        # 이전 after 예약 취소
        if self._laboratorio_filter_after_id is not None:
            self.root.after_cancel(self._laboratorio_filter_after_id)

        # 150ms 뒤에 실제 필터 실행 (디바운스)
        self._laboratorio_filter_after_id = self.root.after(
            150,
            lambda: self._aplicar_filtro_elementos(texto)
        )

    def _aplicar_filtro_elementos(self, texto):
        if not texto:
            filtrados = self.elementos_nombres
        else:
            filtrados = [
                nombre for nombre in self.elementos_nombres
                if texto in nombre
            ]
        self.combo_elemento["values"] = filtrados

    def _aplicar_filtro_laboratorios(self, texto):
        if not texto:
            filtrados = self.laboratorios_nombres
        else:
            filtrados = [
                nombre for nombre in self.laboratorios_nombres
                if texto in nombre
            ]
        self.combo_laboratorio["values"] = filtrados

    def get_datos(self):
        return {
            "placa": self.placa_var.get().strip(),
            "elemento_desc": self.elemento_var.get().strip(),
            "laboratorio_nombre": self.laboratorio_var.get().strip(),
        }
    
    def set_datos(self, datos):
        # 파라미터로 들어오는 datos 딕셔너리의 키값은 
        # 사용하시는 DTO나 DB 구조에 따라 유연하게 변경해 주세요.
        self.placa_var.set(datos.get("placa", ""))
        self.elemento_var.set(datos.get("elemento_desc", ""))
        self.laboratorio_var.set(datos.get("laboratorio_nombre", ""))