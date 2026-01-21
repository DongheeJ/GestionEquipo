import tkinter as tk
from tkinter import ttk
from model.PrestamoDTO import PrestamoDTO
from typing import List

class List_prestamo_view:
    def __init__(self, root):
        self.root = root
        self.root.title("Préstamo de equipo")
        self.root.state('zoomed')
        width, height = 1000, 600
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw // 2) - (width // 2)
        y = (sh // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.root.resizable(True, True)

        # ---------------- 상단 필터 UI (기존 그대로) ----------------
# ---------------- 상단 필터 및 버튼 영역 ----------------
        top_frame = tk.Frame(self.root)
        top_frame.grid(row=0, column=0, sticky="ew", pady=10)
        
        # 중앙 정렬을 원하시면 이 프레임을 하나 더 감싸는 게 좋습니다.
        container = tk.Frame(top_frame)
        container.pack(anchor="center") # 전체를 중앙으로

        # 1. 왼쪽: 필터 영역 (Checkbuttons & Entries)
        filtros_frame = tk.Frame(container)
        filtros_frame.pack(side="left", padx=10)

        self.multado_var = tk.BooleanVar(value=False)
        tk.Checkbutton(filtros_frame, text="Multados", variable=self.multado_var).grid(row=0, column=0, sticky="w")
        
        self.no_entregados_var = tk.BooleanVar(value=False)
        tk.Checkbutton(filtros_frame, text="No entregados", variable=self.no_entregados_var).grid(row=1, column=0, sticky="w")
        
        self.entregados_var = tk.BooleanVar(value=False)
        tk.Checkbutton(filtros_frame, text="Entregados", variable=self.entregados_var).grid(row=2, column=0, sticky="w")

        # 입력창 (2~3열)
        self.estudiante_var = tk.StringVar()
        tk.Label(filtros_frame, text='Estudiante\ncódigo o cedula', font=('calibre',8,'bold')).grid(row=0, column=2, padx=10)
        tk.Entry(filtros_frame, textvariable=self.estudiante_var, width=15).grid(row=0, column=3, padx=5)

        self.equipo_var = tk.StringVar()
        tk.Label(filtros_frame, text='Equipo\nplaca', font=('calibre',8,'bold')).grid(row=1, column=2, padx=10)
        tk.Entry(filtros_frame, textvariable=self.equipo_var, width=15).grid(row=1, column=3, padx=5)

        # 2. 오른쪽: 버튼 영역 (옆으로 나란히 배치)
        boton_frame = tk.Frame(container)
        boton_frame.pack(side="left", padx=20) # filtros_frame 바로 오른쪽에 붙음

        # 버튼들을 세로로 쌓기 위해 fill="x" 유지
        self.btn_aplicar_filtros = tk.Button(boton_frame, text="Aplicar filtros", width=15)
        self.btn_aplicar_filtros.pack(pady=2)

        self.btn_listar_todos = tk.Button(boton_frame, text="Listar todos", width=15)
        self.btn_listar_todos.pack(pady=2)

        self.btn_registrar = tk.Button(boton_frame, text="Registrar", width=15, bg="#e1e1e1")
        self.btn_registrar.pack(pady=2)

        # ---------------- 테이블 영역 (Treeview로 교체) ----------------
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        frame_table = tk.Frame(self.root)
        frame_table.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        columnas = (
            "ID", "Inicio", "Final", "Multa",
            "Estudiante", "Equipo",
            "Ver consumibles", "Pagar multa", "Entregar", "Eliminar" # 10번째에 Eliminar 배치
        )

        self.tabla = ttk.Treeview(frame_table, columns=columnas, show="headings")
        for col in columnas:
            self.tabla.heading(col, text=col)

        # 컬럼 폭(원하는대로 조정 가능)
        self.tabla.column("ID", width=60, anchor="center")
        self.tabla.column("Inicio", width=130, anchor="center")
        self.tabla.column("Final", width=130, anchor="center")
        self.tabla.column("Multa", width=80, anchor="center")
        self.tabla.column("Estudiante", width=160)
        self.tabla.column("Equipo", width=250)
        self.tabla.column("Ver consumibles", width=120, anchor="center")
        self.tabla.column("Pagar multa", width=120, anchor="center")
        self.tabla.column("Entregar", width=120, anchor="center")
        self.tabla.column("Eliminar", width=100, anchor="center")
        # 스크롤바 (Estudiante_view와 동일)
        scrollbar_y = ttk.Scrollbar(frame_table, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar_y.set)

        self.tabla.pack(side="left", fill="both", expand=True)
        scrollbar_y.pack(side="right", fill="y")

        # 클릭 이벤트 방식도 동일하게
        self.tabla.bind("<Button-1>", self._on_click_cell)
        
        # 핸들러
        self.on_ver_consumibles = None
        self.on_pagar_multa = None
        self.on_entregar = None
        self.on_eliminar = None
        # row_id -> PrestamoDTO 매핑 (클릭 시 DTO 얻기 위해)
        self._row_to_prestamo = {}

    # def _toggle_radio(self):
    #     """라디오 버튼 토글 로직: 이미 선택된 것을 누르면 해제"""
    #     current_val = self.estado_var.get()
    #     if current_val == self.last_selected:
    #         self.estado_var.set(0)
    #         self.last_selected = 0
    #     else:
    #         self.last_selected = current_val

    def get_estudiante(self):
        return self.estudiante_var.get()
    def get_placa(self):
        return self.equipo_var.get()
    def get_multados(self):
        return self.multado_var.get()
    def get_no_entregados(self):
        return self.no_entregados_var.get()
    def get_entregados(self):
        return self.entregados_var.get()
    
    def set_estudiante(self,estudiante):
        self.estudiante_var.set(estudiante)

    def set_placa(self,placa):
        self.equipo_var.set(placa)

    def set_multados(self,value):
        self.multado_var.set(value)

    def set_no_entregados(self,value):
        self.no_entregados_var.set(value)

    def set_entregados(self,value):
        self.entregados_var.set(value)
    
    def set_ver_consumibles_handler(self, handler):
        self.on_ver_consumibles = handler

    def set_pagar_multa_handle(self, handler):
        self.on_pagar_multa = handler

    def set_entregar_handle(self, handler):
        self.on_entregar = handler

    def set_eliminar_handle(self, handler):
        self.on_eliminar = handler

    def _on_click_cell(self, event):
        region = self.tabla.identify("region", event.x, event.y)
        if region != "cell":
            return

        col = self.tabla.identify_column(event.x)  # "#1", "#2", ...
        row_id = self.tabla.identify_row(event.y)
        if not row_id:
            return

        prestamo = self._row_to_prestamo.get(row_id)
        if not prestamo:
            return

        # 컬럼 번호(8개)
        col_ver = "#7"    # Ver consumibles
        col_pagar = "#8"  # Pagar multa
        col_entregar ="#9"
        col_eliminar = "#10"

        if col == col_ver and self.on_ver_consumibles:
            self.on_ver_consumibles(prestamo)
        elif col == col_pagar and self.on_pagar_multa:
            self.on_pagar_multa(prestamo)
        elif col == col_entregar and self.on_entregar:
            self.on_entregar(prestamo)
        elif col == col_eliminar and self.on_eliminar: # Eliminar 클릭 시
                    self.on_eliminar(prestamo)

    def render(self, prestamos: List[PrestamoDTO]):
        # 기존 행 삭제
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        self._row_to_prestamo.clear()

        if not prestamos:
            return

        for p in prestamos:
            id_prestamo = p.get_idPrestamo()
            hora_inicio = p.get_hora_inicio()
            hora_final  = p.get_hora_final()
            multa       = p.get_multa()

            nombre_estudiante = p.get_estudiante().get_nombre()
            equipo_info = (
                p.get_equipo().get_Elemento().get_descripcion()
                + " - "
                + p.get_equipo().get_placa()
            )

            row = (
                id_prestamo,
                hora_inicio,
                hora_final,
                multa,
                nombre_estudiante,
                equipo_info,
                "Ver",
                "Pagar",
                "Entregar",
                "Eliminar"
            )

            item_id = self.tabla.insert("", "end", values=row)
            self._row_to_prestamo[item_id] = p
