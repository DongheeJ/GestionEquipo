import tkinter as tk
from tkinter import ttk, messagebox

class RegistrarEquipo_view:
    def __init__(self, root):
        self.root = root
        width, height = 400, 300
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.root.title("Registrar equipo")
        
        self.map_elementos = {}
        self.elementos_descripciones = []
        self._elemento_filter_after_id = None  

        self.map_laboratorios = {}
        self.laboratorios_nombres = []
        self._laboratorio_filter_after_id = None  

        # ====== 상단 입력 프레임 ======
        frame_form = tk.Frame(root)
        frame_form.pack(padx=20, pady=30)

        # Placa
        tk.Label(frame_form, text="Placa:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_placa = tk.Entry(frame_form, width=25)
        self.entry_placa.grid(row=0, column=1, padx=5, pady=5)

        # Elemento (FK)
        tk.Label(frame_form, text="Elemento:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.combo_elemento = ttk.Combobox(frame_form, state="normal", width=30)
        self.combo_elemento.grid(row=1, column=1, padx=5, pady=5)

        # Laboratorio (FK)
        tk.Label(frame_form, text="Laboratorio:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.combo_laboratorio = ttk.Combobox(frame_form, state="normal", width=30)
        self.combo_laboratorio.grid(row=2, column=1, padx=5, pady=5)

        # ====== 버튼 프레임 ======
        frame_btn = tk.Frame(root)
        frame_btn.pack(pady=20)

        # 컨트롤러에서 command를 연결해줄 버튼
        self.btn_registrar = tk.Button(frame_btn, text="Registrar equipo")
        self.btn_registrar.grid(row=0, column=0, padx=10)

        self.btn_cancelar = tk.Button(frame_btn, text="Cancelar", command=root.destroy)
        self.btn_cancelar.grid(row=0, column=1, padx=10)

    def cargar_elementos(self, elementos):
        self.map_elementos = {desc: _id for _id, desc in elementos}
        self.elementos_descripciones = list(self.map_elementos.keys())

        self.combo_elemento["values"] = self.elementos_descripciones

        # 키 입력 시 필터 (디바운스 적용)
        self.combo_elemento.bind("<KeyRelease>", self._filtrar_elementos_debounced)


    def _filtrar_elementos_debounced(self, event=None):
        texto = self.combo_elemento.get()

        # 이전에 예약된 after 있으면 취소
        if self._elemento_filter_after_id is not None:
            self.root.after_cancel(self._elemento_filter_after_id)

        # 150ms 뒤에 진짜 필터 적용
        self._elemento_filter_after_id = self.root.after(
            150,
            lambda: self._aplicar_filtro_elementos(texto)
        )

    def _aplicar_filtro_elementos(self, texto):
        if not texto:
            filtrados = self.elementos_descripciones
        else:
            filtrados = [
                desc for desc in self.elementos_descripciones
                if texto in desc
            ]

        self.combo_elemento["values"] = filtrados

    def cargar_laboratorios(self, laboratorios):
        """
        laboratorios: [(idLaboratorio, nombre), ...]
        """
        self.map_laboratorios = {nombre: _id for _id, nombre in laboratorios}
        self.laboratorios_nombres = list(self.map_laboratorios.keys())

        self.combo_laboratorio["values"] = self.laboratorios_nombres

        # 🔹 laboratorio 검색용 필터 바인딩
        self.combo_laboratorio.bind("<KeyRelease>", self._filtrar_laboratorios_debounced)

    def _filtrar_laboratorios_debounced(self, event=None):
        texto = self.combo_laboratorio.get()

        if self._laboratorio_filter_after_id is not None:
            self.root.after_cancel(self._laboratorio_filter_after_id)

        self._laboratorio_filter_after_id = self.root.after(
            150,
            lambda: self._aplicar_filtro_laboratorios(texto)
        )

    def _aplicar_filtro_laboratorios(self, texto):
        if not texto:
            filtrados = self.laboratorios_nombres
        else:
            filtrados = [
                nombre for nombre in self.laboratorios_nombres
                if texto in nombre
            ]

        self.combo_laboratorio["values"] = filtrados

    # ---------- getter들 (컨트롤러에서 insert 할 때 사용) ----------
    def get_placa(self):
        return self.entry_placa.get().strip()

    def get_id_elemento(self):
        desc = self.combo_elemento.get()
        return self.map_elementos.get(desc)

    def get_id_laboratorio(self):
        nombre = self.combo_laboratorio.get()
        return self.map_laboratorios.get(nombre)

    def get_datos_equipo(self):
        return {
            "placa": self.get_placa(),
            "idElemento": self.get_id_elemento(),
            "idLaboratorio": self.get_id_laboratorio()
        }

    # ---------- 메시지 도우미 ----------
    def mostrar_mensaje(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)
        
    def mostrar_error(self, titulo, mensaje):
        messagebox.showerror(titulo, mensaje)

    def confirmar(self,titulo,mensaje):
        return messagebox.askyesno(titulo,mensaje)