import tkinter as tk
from tkinter import ttk
from model.Proyecto_C_DTO import Proyecto_C_DTO
from typing import List

class ProyectoC_view:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de proyecto curricular")

        self.root.state('zoomed')
        # --- 창 크기 및 중앙 배치 설정 ---
        width, height = 1000, 600
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        x = (sw // 2) - (width // 2)
        y = (sh // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.root.resizable(True, True)
        
        # ================= 필터 프레임 =================
        frame_filtros = tk.Frame(root)
        frame_filtros.pack(pady=10)

        tk.Label(frame_filtros, text="nombre del proyecto curricular:").grid(row=2, column=2, padx=5, pady=5)
        self.nombre_var = tk.StringVar()
        self.entry_nombre = tk.Entry(frame_filtros, textvariable=self.nombre_var)
        self.entry_nombre.grid(row=2, column=3, padx=5, pady=5)

        # ---- aplicar filtros 버튼 ----
        self.btn_aplicar_filtros = tk.Button(frame_filtros, text="Aplicar filtros")
        self.btn_aplicar_filtros.grid(row=0, column=3, padx=10, pady=5)

        # 버튼 프레임
        frame_btn = tk.Frame(root)
        frame_btn.pack(pady=10)

        self.btn_listar = tk.Button(frame_btn, text="Listar proyectos")
        self.btn_listar.grid(row=0, column=0, padx=5)

        self.btn_registrar = tk.Button(frame_btn, text="Registrar proyecto")
        self.btn_registrar.grid(row=0, column=1, padx=5)

        # ================= 테이블 컨테이너 =================
        frame_table = tk.Frame(root)
        frame_table.pack(padx=10, pady=10, fill="both", expand=True)

        # 세로 스크롤바
        scroll_y = ttk.Scrollbar(frame_table, orient="vertical")
        # 가로 스크롤바 (선택)
        scroll_x = ttk.Scrollbar(frame_table, orient="horizontal")

        self.tabla = ttk.Treeview(
            frame_table,
            columns=("ID", "Nombre", "Editar", "Eliminar"),
            show="headings",
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set
        )

        scroll_y.config(command=self.tabla.yview)
        scroll_x.config(command=self.tabla.xview)

        # 헤더
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Editar", text="Editar")
        self.tabla.heading("Eliminar", text="Eliminar")

        # 컬럼 폭
        self.tabla.column("ID", width=150, anchor="center")
        self.tabla.column("Nombre", width=250)
        self.tabla.column("Editar", width=150, anchor="center")
        self.tabla.column("Eliminar", width=150, anchor="center")

        # 배치
        self.tabla.grid(row=0, column=0, sticky="nsew")
        scroll_y.grid(row=0, column=1, sticky="ns")
        scroll_x.grid(row=1, column=0, sticky="ew")

        frame_table.rowconfigure(0, weight=1)
        frame_table.columnconfigure(0, weight=1)

        self.on_editar = None
        self.on_eliminar = None
        self.tabla.bind("<Button-1>", self._on_click_cell)

    def mostrar_tabla(self, proyectos: List[Proyecto_C_DTO]):
        # 1) 기존 행 삭제
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        # 2) 비어있으면 종료
        if not proyectos:
            return

        # 3) DTO -> row 변환해서 insert
        for p in proyectos:
            row = (
                p.get_idProyecto_C(),
                p.get_nombre(),
                "Editar",
                "Eliminar",
            )
            # iid에 id를 박아두면 클릭 시 식별이 편함(추천)
            self.tabla.insert("", "end", iid=str(p.get_idProyecto_C()), values=row)

    def get_filtro_nombre(self):
        return self.nombre_var.get().strip()
    
    def set_editar_handler(self, handler):
        self.on_editar = handler
    def set_eliminar_handler(self, handler):
        self.on_eliminar = handler

    def _on_click_cell(self, event):
        region = self.tabla.identify("region", event.x, event.y)
        if region != "cell":
            return

        col = self.tabla.identify_column(event.x)  # "#1" ~
        row_id = self.tabla.identify_row(event.y)
        if not row_id:
            return

        values = self.tabla.item(row_id, "values")
        if not values:
            return

        id_proyecto = int(values[0])  # ID 컬럼
        nombre = values[1]

        col_editar = "#3"    # Editar
        col_eliminar = "#4"  # Eliminar
        
        proyecto = Proyecto_C_DTO(id_proyecto,nombre)
        if col == col_editar and self.on_editar:
            self.on_editar(proyecto)

        elif col == col_eliminar and self.on_eliminar:
            self.on_eliminar(id_proyecto)