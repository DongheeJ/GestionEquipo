import tkinter as tk
from tkinter import ttk
from model.LaboratorioDTO import LaboratorioDTO
from typing import List

class Laboratorio_view:
    def __init__(self, root):
        self.root = root
        # self.root.title("Gestión de laboratorio")

        # self.root.state('zoomed')
        # # --- 창 크기 및 중앙 배치 설정 ---
        # width, height = 1000, 600
        # sw = self.root.winfo_screenwidth()
        # sh = self.root.winfo_screenheight()
        # x = (sw // 2) - (width // 2)
        # y = (sh // 2) - (height // 2)
        # self.root.geometry(f"{width}x{height}+{x}+{y}")
        # self.root.resizable(True, True)
        
        # ================= 필터 프레임 =================
        frame_filtros = tk.Frame(root)
        frame_filtros.pack(pady=10)

        tk.Label(frame_filtros, text="nombre del laboratorio:").grid(row=2, column=2, padx=5, pady=5)
        self.nombre_var = tk.StringVar()
        self.entry_nombre = tk.Entry(frame_filtros, textvariable=self.nombre_var)
        self.entry_nombre.grid(row=2, column=3, padx=5, pady=5)

        # ---- aplicar filtros 버튼 ----
        self.btn_aplicar_filtros = tk.Button(frame_filtros, text="Aplicar filtros")
        self.btn_aplicar_filtros.grid(row=0, column=3, padx=10, pady=5)

        # 버튼 프레임
        frame_btn = tk.Frame(root)
        frame_btn.pack(pady=10)

        self.btn_listar = tk.Button(frame_btn, text="Listar laboratorios")
        self.btn_listar.grid(row=0, column=0, padx=5)

        self.btn_registrar = tk.Button(frame_btn, text="Registrar laboratorios")
        self.btn_registrar.grid(row=0, column=1, padx=5)

        self.btn_eliminar_multi = tk.Button(frame_btn, text="Eliminar seleccionados", bg="#ffcccc")
        self.btn_eliminar_multi.grid(row=0, column=2, padx=5)
        
        frame_table = tk.Frame(root)
        frame_table.pack(padx=10, pady=10, fill="both", expand=True)

        # 세로 스크롤바
        scroll_y = ttk.Scrollbar(frame_table, orient="vertical")
        # 가로 스크롤바 (선택)
        scroll_x = ttk.Scrollbar(frame_table, orient="horizontal")

        # 테이블 (Treeview)
        self.tabla = ttk.Treeview(
            frame_table,
            columns=("ID", "Nombre","Editar","Eliminar"),
            show="headings",
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set
        )

        scroll_y.config(command=self.tabla.yview)
        scroll_x.config(command=self.tabla.xview)

        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("Editar", text="Editar")
        self.tabla.heading("Eliminar", text="Eliminar")

        self.tabla.column("ID", width=150)
        self.tabla.column("Nombre", width=200)
        self.tabla.column("Editar", width=200)
        self.tabla.column("Eliminar", width=200)

        # 배치
        self.tabla.grid(row=0, column=0, sticky="nsew")
        scroll_y.grid(row=0, column=1, sticky="ns")
        scroll_x.grid(row=1, column=0, sticky="ew")

        frame_table.rowconfigure(0, weight=1)
        frame_table.columnconfigure(0, weight=1)

        self.on_editar = None
        self.on_eliminar = None
        self.tabla.bind("<Button-1>", self._on_click_cell)

    def mostrar_tabla(self, proyectos: List[LaboratorioDTO]):
        # 1) 기존 행 삭제
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        # 2) 비어있으면 종료
        if not proyectos:
            return

        # 3) DTO -> row 변환해서 insert
        for p in proyectos:
            row = (
                p.get_idLaboratorio(),
                p.get_nombre(),
                "Editar",
                "Eliminar",
            )
            # iid에 id를 박아두면 클릭 시 식별이 편함(추천)
            self.tabla.insert("", "end", iid=str(p.get_idLaboratorio()), values=row)

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

        idLaboratorio = int(values[0])  # ID 컬럼
        nombre = values[1]

        col_editar = "#3"    # Editar
        col_eliminar = "#4"  # Eliminar
        
        laboratorio = LaboratorioDTO(idLaboratorio,nombre)
        if col == col_editar and self.on_editar:
            self.on_editar(laboratorio)

        elif col == col_eliminar and self.on_eliminar:
            self.on_eliminar(idLaboratorio)

    def get_selected_ids(self):
        items = self.tabla.selection() # 선택된 모든 행의 iid 가져오기
        selected_ids = []
        for item in items:
            values = self.tabla.item(item, "values")
            if values:
                selected_ids.append(int(values[0])) # ID 컬럼값 추출
        return selected_ids