import tkinter as tk
from tkinter import ttk
from model.ElementoDTO import ElementoDTO
from typing import List

class Elemento_view:
    def __init__(self, root):
        self.root = root
        # self.root.title("Gestión de elemento")
        # self.root.state('zoomed')
        # # 1. 창 크기 설정
        # width = 1000  # 테이블이 있으므로 조금 넓게 설정
        # height = 600
        
        # # 2. 화면 중앙 좌표 계산
        # screen_width = self.root.winfo_screenwidth()
        # screen_height = self.root.winfo_screenheight()
        
        # x = (screen_width // 2) - (width // 2)
        # y = (screen_height // 2) - (height // 2)
        
        # # 3. 위치와 크기 적용 ("너비x높이+X좌표+Y좌표")
        # self.root.geometry(f"{width}x{height}+{x}+{y}")

        # ================= 필터 프레임 =================
        frame_filtros = tk.Frame(root)
        frame_filtros.pack(pady=10)

        tk.Label(frame_filtros, text="descripcion del elemento:").grid(row=2, column=2, padx=5, pady=5)
        self.descripcion_var = tk.StringVar()
        self.entry_desc = tk.Entry(frame_filtros, textvariable=self.descripcion_var)
        self.entry_desc.grid(row=2, column=3, padx=5, pady=5)

        # ---- aplicar filtros 버튼 ----
        self.btn_aplicar_filtros = tk.Button(frame_filtros, text="Aplicar filtros")
        self.btn_aplicar_filtros.grid(row=0, column=3, padx=10, pady=5)

        # 버튼 프레임
        frame_btn = tk.Frame(root)
        frame_btn.pack(pady=10)

        self.btn_listar = tk.Button(frame_btn, text="Listar elementos")
        self.btn_listar.grid(row=0, column=0, padx=5)

        self.btn_registrar = tk.Button(frame_btn, text="Registrar elemento")
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
            columns=("ID", "Descripcion","Cantidad","Editar","Eliminar"),
            show="headings",
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set
        )

        scroll_y.config(command=self.tabla.yview)
        scroll_x.config(command=self.tabla.xview)

        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Descripcion", text="Descripcion")
        self.tabla.heading("Cantidad", text="Cantidad")
        self.tabla.heading("Editar", text="Editar")
        self.tabla.heading("Eliminar", text="Eliminar")

        self.tabla.column("ID", width=150)
        self.tabla.column("Descripcion", width=200)
        self.tabla.column("Cantidad", width=200)
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

    def mostrar_tabla(self, elementos: List[ElementoDTO]):
        # 1) 기존 행 삭제
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        # 2) 비어있으면 종료
        if not elementos:
            return

        # 3) DTO -> row 변환해서 insert
        for e in elementos:
            # 여기서 p는 ElementoDTO 타입임을 IDE가 인식합니다.
            row = (
                e.get_idElemento(), # 이제 p. 입력 시 자동 완성이 뜹니다!
                e.get_descripcion(),       # DTO에 정의된 메서드들
                e.get_cantidad(),
                "Editar",
                "Eliminar",
            )
            self.tabla.insert("", "end", iid=str(e.get_idElemento()), values=row)

    def get_filtro_desc(self):
        return self.descripcion_var.get().strip()
    
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

        idElemento = int(values[0])  # ID 컬럼
        descripcion = values[1]
        cantidad = int (values[2])
        col_editar = "#4"    # Editar
        col_eliminar = "#5"  # Eliminar
        
        elemento = ElementoDTO(idElemento,descripcion,cantidad)
        if col == col_editar and self.on_editar:
            self.on_editar(elemento)

        elif col == col_eliminar and self.on_eliminar:
            self.on_eliminar(idElemento)

    def get_selected_ids(self):
        items = self.tabla.selection() # 선택된 모든 행의 iid 가져오기
        selected_ids = []
        for item in items:
            values = self.tabla.item(item, "values")
            if values:
                selected_ids.append(int(values[0])) # ID 컬럼값 추출
        return selected_ids