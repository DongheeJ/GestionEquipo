import tkinter as tk
from tkinter import ttk
from model.EquipoDTO import EquipoDTO  # DTO 클래스가 있다고 가정
from typing import List

class Equipo_view:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Equipos")
        self.root.state('zoomed')
        # --- 창 크기 및 중앙 배치 설정 ---
        width, height = 1000, 600
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw // 2) - (width // 2)
        y = (sh // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.root.resizable(True, True)

        self._elemento_filter_after_id = None
        self._laboratorio_filter_after_id = None
        # ================= 상단 검색 / 필터 프레임 =================
        frame_top = tk.Frame(self.root)
        frame_top.pack(pady=20)

        # Placa
        tk.Label(frame_top, text="Placa:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_placa = tk.Entry(frame_top, width=25)
        self.entry_placa.grid(row=0, column=1, padx=5, pady=5)

        # Elemento (FK)
        tk.Label(frame_top, text="Elemento:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.combo_elemento = ttk.Combobox(frame_top, state="normal", width=30)
        self.combo_elemento.grid(row=1, column=1, padx=5, pady=5)

        # Laboratorio (FK)
        tk.Label(frame_top, text="Laboratorio:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.combo_laboratorio = ttk.Combobox(frame_top, state="normal", width=30)
        self.combo_laboratorio.grid(row=2, column=1, padx=5, pady=5)

        # ================= 라디오 버튼 필터 (상태) =================
        # 토글 기능을 위한 변수 설정
        self.estado_var = tk.IntVar(value=0)
        self.last_selected = 0

        frame_radio = tk.Frame(self.root)
        frame_radio.pack(pady=5)

        self.rb_libre = tk.Radiobutton(
            frame_radio, text="libre", variable=self.estado_var, 
            value=1, command=self._toggle_radio
        )
        self.rb_libre.grid(row=0, column=0, padx=10)

        self.rb_uso = tk.Radiobutton(
            frame_radio, text="en uso", variable=self.estado_var, 
            value=2, command=self._toggle_radio
        )
        self.rb_uso.grid(row=0, column=1, padx=10)

        # aplicar filtros 버튼
        self.btn_aplicar_filtros = tk.Button(frame_top, text="Aplicar filtros")
        self.btn_aplicar_filtros.grid(row=0, column=4, rowspan=2, padx=20)

        # ================= 버튼 프레임 (listar / registrar) =================
        frame_btn = tk.Frame(self.root)
        frame_btn.pack(pady=10)

        self.btn_listar = tk.Button(frame_btn, text="Listar equipos")
        self.btn_listar.grid(row=0, column=0, padx=5)

        self.btn_registrar = tk.Button(frame_btn, text="Registrar equipo")
        self.btn_registrar.grid(row=0, column=1, padx=5)

        # ================= 테이블 (Treeview) =================
        columnas = ("ID", "Placa", "Elemento", "Laboratorio", "Estado", "Editar", "Eliminar")
        
        self.tabla = ttk.Treeview(self.root, columns=columnas, show="headings")

        # 헤더 설정
        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, anchor="center")

        self.tabla.column("ID", width=50)
        self.tabla.column("Placa", width=120)
        self.tabla.column("Elemento", width=180)
        self.tabla.column("Laboratorio", width=180)
        self.tabla.column("Estado", width=100)
        self.tabla.column("Editar", width=100)
        self.tabla.column("Eliminar", width=100)

        # 이벤트 핸들러 및 바인딩
        self.on_editar = None
        self.on_eliminar = None
        self.tabla.bind("<Button-1>", self._on_click_cell)

        # 스크롤바
        scrollbar_y = ttk.Scrollbar(self.root, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar_y.set)

        self.tabla.pack(side="left", fill="both", expand=True, padx=(20, 0), pady=20)
        scrollbar_y.pack(side="right", fill="y", padx=(0, 20), pady=20)

    # ================= 내부 로직 메서드 =================
    def _toggle_radio(self):
        """라디오 버튼 토글 로직: 이미 선택된 것을 누르면 해제"""
        current_val = self.estado_var.get()
        if current_val == self.last_selected:
            self.estado_var.set(0)
            self.last_selected = 0
        else:
            self.last_selected = current_val

    def _on_click_cell(self, event):
        region = self.tabla.identify("region", event.x, event.y)
        if region != "cell": return

        col = self.tabla.identify_column(event.x)
        row_id = self.tabla.identify_row(event.y)
        if not row_id: return

        values = self.tabla.item(row_id, "values")
        if not values: return

        # DTO 구성을 위한 데이터 추출
        # (ID, Placa, Elemento, Laboratorio, Estado, Editar, Eliminar)
        id_eq = values[0]
        placa = values[1]
        elemento_desc = values[2]
        laboratorio_nombre = values[3]
        estado = values[4]

        # 컬럼 인덱스 매칭
        if col == "#6" and self.on_editar:   # Editar
            # 여기서 필요시 DTO 객체를 생성하여 넘깁니다.
            equipo = EquipoDTO(id_eq,placa)
            self.on_editar(equipo,elemento_desc,laboratorio_nombre)
        elif col == "#7" and self.on_eliminar: # Eliminar
            equipo = EquipoDTO(id_eq,placa)
            self.on_eliminar(equipo,estado)

    # ================= 외부 공개 메서드 (API) =================
    def mostrar_tabla(self, equipos: List[EquipoDTO]):
        """DTO 리스트를 받아 테이블을 그림"""
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        if not equipos: return

        for eq in equipos:
            # DTO 구조에 맞춰 getter 호출 (예시)
            row = (
                eq.get_idEquipo(),
                eq.get_placa(),
                eq.get_Elemento().get_descripcion() if eq.get_Elemento() else "",
                eq.get_Laboratorio().get_nombre() if eq.get_Laboratorio() else "",
                eq.get_Estado().get_descripcion(), # "libre" or "en uso"
                "Editar",
                "Eliminar"
            )
            self.tabla.insert("", "end", values=row)

    def get_placa(self):
        return self.entry_placa.get()
    
    def get_elemento(self):
        return self.combo_elemento.get()

    def get_laboratorio(self):
        return self.combo_laboratorio.get()
    
    def get_filtros_estado(self):
        val = self.estado_var.get()
        estado = ""
        if val == 1: estado = "libre"
        elif val == 2: estado = "en uso"

        return estado

    def set_editar_handler(self, handler):
        self.on_editar = handler

    def set_eliminar_handler(self, handler):
        self.on_eliminar = handler

    def cargar_elementos(self, elementos):
        map_elementos = {desc: _id for _id, desc in elementos}
        self.elementos_descripciones = list(map_elementos.keys())

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
        map_laboratorios = {nombre: _id for _id, nombre in laboratorios}
        self.laboratorios_nombres = list(map_laboratorios.keys())

        self.combo_laboratorio["values"] = self.laboratorios_nombres

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
