import tkinter as tk
from tkinter import ttk
from model.EstudianteDTO import EstudianteDTO
from typing import List

class Estudiante_view:
    def __init__(self, root):
        self.root = root
        # self.root.title("Gestión de Estudiantes")
        # self.root.state('zoomed')
        # # --- 창 크기 및 중앙 배치 설정 ---
        # width, height = 1000, 600
        # sw = self.root.winfo_screenwidth()
        # sh = self.root.winfo_screenheight()
        # x = (sw // 2) - (width // 2)
        # y = (sh // 2) - (height // 2)
        # self.root.geometry(f"{width}x{height}+{x}+{y}")
        # self.root.resizable(True, True)

        self._proyecto_filter_after_id = None
        # =============== 상단 검색 (codigo / cedula) ===============
        frame_form = tk.Frame(self.root)
        frame_form.pack(pady=20)

        tk.Label(frame_form, text="Código / Cédula:").grid(row=0, column=0, padx=5)
        self.entry_estudiante = tk.Entry(frame_form, width=25)
        self.entry_estudiante.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Proyecto curricular:").grid(row=1, column=0, padx=5)
        self.combo_proyecto_c =  ttk.Combobox(frame_form, state="normal", width=30)
        self.combo_proyecto_c.grid(row=1, column=1, padx=5, pady=5)

        # =============== 필터 프레임 ===============
        frame_filtros = tk.Frame(self.root)
        frame_filtros.pack(pady=10)

        self.multado_var = tk.BooleanVar(value=False)
        self.chk_multado = tk.Checkbutton(
            frame_filtros,
            text="multado",
            variable=self.multado_var
        )
        self.chk_multado.grid(row=0, column=0, padx=5, pady=5)

        self.no_entregado_var = tk.BooleanVar(value=False)
        self.chk_no_entregado = tk.Checkbutton(
            frame_filtros,
            text="equipos no entregados",
            variable=self.no_entregado_var
        )
        self.chk_no_entregado.grid(row=0, column=1, padx=5, pady=5)

        # ---- aplicar filtros 버튼 ----
        self.btn_aplicar_filtros = tk.Button(frame_filtros, text="Aplicar filtros")
        self.btn_aplicar_filtros.grid(row=0, column=4, rowspan=2, padx=15, pady=5)

        # =============== 버튼 프레임 (listar / registrar) ===============
        frame_btn = tk.Frame(root)
        frame_btn.pack(pady=10)

        self.btn_listar = tk.Button(frame_btn, text="Listar estudiantes")
        self.btn_listar.grid(row=0, column=0, padx=5)

        self.btn_registrar = tk.Button(frame_btn, text="Registrar estudiante")
        self.btn_registrar.grid(row=0, column=1, padx=5)

        self.btn_eliminar_multi = tk.Button(frame_btn, text="Eliminar seleccionados", bg="#ffcccc")
        self.btn_eliminar_multi.grid(row=0, column=2, padx=5)
        
        # =============== 테이블 (Treeview) ===============
        columnas = (
            "ID", "Nombre", "Apellido",
            "Correo", "Celular",
            "Código", "Cédula",
            "Proyecto", "Ver prestamos", "Editar", "Eliminar"
        )

        self.tabla = ttk.Treeview(
            root,
            columns=columnas,
            show="headings"
        )

        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Apellido", text="Apellido")
        self.tabla.heading("Correo", text="Correo")
        self.tabla.heading("Celular", text="Celular")
        self.tabla.heading("Código", text="Código")
        self.tabla.heading("Cédula", text="Cédula")
        self.tabla.heading("Proyecto", text="Proyecto")
        self.tabla.heading("Ver prestamos", text="Ver prestamos")
        self.tabla.heading("Editar", text="Editar")
        self.tabla.heading("Eliminar", text="Eliminar")

        self.tabla.column("ID", width=60, anchor="center")
        self.tabla.column("Nombre", width=120)
        self.tabla.column("Apellido", width=120)
        self.tabla.column("Correo", width=180)
        self.tabla.column("Celular", width=100)
        self.tabla.column("Código", width=100)
        self.tabla.column("Cédula", width=100)
        self.tabla.column("Proyecto", width=150)
        self.tabla.column("Ver prestamos", width=110, anchor="center")
        self.tabla.column("Editar", width=110, anchor="center")
        self.tabla.column("Eliminar", width=110, anchor="center")

        self.on_ver_prestamos = None
        self.on_editar = None
        self.on_eliminar = None

        self.tabla.bind("<Button-1>", self._on_click_cell)

        # 스크롤바 추가 (선택)
        scrollbar_y = ttk.Scrollbar(root, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar_y.set)

        self.tabla.pack(side="left", fill="both", expand=True, pady=20)
        scrollbar_y.pack(side="right", fill="y")

    def get_estudiante_seleccionado(self):
        selected = self.tabla.focus()
        if not selected:
            return None
        values = self.tabla.item(selected, "values")
        if not values:
            return None
        return values[5]   # 첫 번째 컬럼이 ID라고 가정
    
    def set_ver_prestamos_handler(self, handler):
        """컨트롤러에서 콜백을 등록할 때 사용"""
        self.on_ver_prestamos = handler

    def set_editar_handler(self, handler):
        self.on_editar = handler

    def set_eliminar_handler(self,handler):
        self.on_eliminar = handler

    def _on_click_cell(self, event):
        # 어느 영역인지 확인
        region = self.tabla.identify("region", event.x, event.y)
        if region != "cell":
            return

        # 클릭한 컬럼, 행 찾기
        col = self.tabla.identify_column(event.x)  # "#1", "#2", ...
        row_id = self.tabla.identify_row(event.y)
        if not row_id:
            return

        values = self.tabla.item(row_id, "values")
        if not values:
            return

        # 여기서 무엇을 넘길지 결정 (ID or Código)
        # ID를 넘기고 싶으면 values[0], código 넘기고 싶으면 values[5]
        id = values[0]
        nombre = values[1]
        apellido = values[2]
        correo = values[3]
        celular = values[4]
        codigo = values[5]
        cedula = values[6]
        proyecto = values[7]

        # 컬럼 인덱스
        col_ver = "#9"      # "Ver prestamos"
        col_editar = "#10"  # "Editar"
        col_eliminar = "#11" # Eliminar 

        if col == col_ver and self.on_ver_prestamos:
            self.on_ver_prestamos(codigo,self.multado_var.get(),self.no_entregado_var.get())
        elif col == col_editar and self.on_editar:
            estudiante = EstudianteDTO(id,nombre,apellido,correo,celular,codigo,cedula)
            self.on_editar(estudiante,proyecto)
        elif col == col_eliminar and self.on_eliminar:
            estudiante = EstudianteDTO(id,nombre,apellido,correo,celular,codigo,cedula)
            self.on_eliminar(estudiante)

    # =================== 테이블 그리기 ===================
    def mostrar_tabla(self, estudiantes: List[EstudianteDTO]):
        # estudiantes: list[EstudianteDTO] 또는 기존처럼 list[tuple] 둘 다 허용

        # 1) 기존 행 삭제
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        # 2) 비어있으면 종료
        if not estudiantes:
            return

        # 3) 이미 튜플/리스트로 들어오면 그대로 insert (기존 호환)
        first = estudiantes[0]
        if isinstance(first, (tuple, list)):
            for d in estudiantes:
                self.tabla.insert("", "end", values=d)
            return

        # 4) DTO 객체로 들어오면 View에서 row로 변환해서 insert
        for e in estudiantes:
            proyecto_nombre = ""
            # e.get_proyecto_c()가 있다면 사용, 없고 문자열만 따로 들고 있으면 그걸 쓰도록 확장 가능
            if hasattr(e, "get_proyecto_c") and e.get_proyecto_c():
                proyecto_nombre = e.get_proyecto_c().get_nombre()

            row = (
                e.get_idEstudiante(),
                e.get_nombre(),
                e.get_apellido(),
                e.get_correo(),
                e.get_celular(),
                e.get_codigo(),
                e.get_cedula(),
                proyecto_nombre,
                "Ver",
                "Editar",
                "Eliminar"
            )
            self.tabla.insert("", "end", values=row)

# =================== 필터 값 꺼내기 ===================
    def get_selected_ids(self):
        items = self.tabla.selection() # 선택된 모든 행의 iid 가져오기
        selected_ids = []
        for item in items:
            values = self.tabla.item(item, "values")
            if values:
                selected_ids.append(int(values[0])) # ID 컬럼값 추출
        return selected_ids
    
    def get_busqueda_codigo_cedula(self):
        return self.entry_estudiante.get().strip()

    def get_filtro_proyecto(self):
        return self.combo_proyecto_c.get().strip()

    def get_filtro_multado(self):
        return self.multado_var.get()

    def get_filtro_no_entregado(self):
        return self.no_entregado_var.get()

    def cargar_proyectos(self, proyectos):
        # 1. self.map_proyectos로 인스턴스 변수화하여 나중에 ID를 찾을 수 있게 함
        # "None" 항목을 가장 먼저 추가
        self.map_proyectos = {"None": None}
        for _id, desc in proyectos:
            self.map_proyectos[desc] = _id

        # 2. 리스트 생성 (딕셔너리의 키를 가져오면 "None"이 맨 앞에 옴)
        self.proyectos_nombres = list(self.map_proyectos.keys())

        # 3. 콤보박스에 값 설정 및 텍스트 비우기
        self.combo_proyecto_c["values"] = self.proyectos_nombres
        self.combo_proyecto_c.set('')

        # 키 입력 시 필터 (디바운스 적용)
        self.combo_proyecto_c.bind("<KeyRelease>", self._filtrar_proyectos_debounced)

    def _filtrar_proyectos_debounced(self, event=None):
        texto = self.combo_proyecto_c.get()

        # 이전에 예약된 after 있으면 취소
        if self._proyecto_filter_after_id is not None:
            self.root.after_cancel(self._proyecto_filter_after_id)

        # 150ms 뒤에 진짜 필터 적용
        self._proyecto_filter_after_id = self.root.after(
            150,
            lambda: self._aplicar_filtro_proyectos(texto)
        )

    def _aplicar_filtro_proyectos(self, texto):
        if not texto:
            # 텍스트가 없으면 전체 리스트 ("None" 포함) 보여줌
            filtrados = self.proyectos_nombres
        else:
            # 검색 시에도 "None"은 맨 위에 유지, 나머지는 검색어 필터링 (대소문자 무시)
            filtrados = ["None"] + [
                desc for desc in self.proyectos_nombres
                if desc != "None" and (texto.lower() in desc.lower())
            ]

        self.combo_proyecto_c["values"] = filtrados