import tkinter as tk
from service.Equipo_service import Equipo_service

from view.Equipo_view import Equipo_view
from controller.Equipo_controller import Equipo_controller

from service.Prestamo_service import Prestamo_service
from service.Consumible_service import Consumible_service
from service.Estudiante_service import Estudiante_service

from controller.List_prestamo_controller import List_prestamo_controller
from view.List_prestamo_view import List_prestamo_view

from view.Estudiante_view import Estudiante_view
from controller.Estudiante_controller import Estudiante_controller

from view.ProyectoC_view import ProyectoC_view
from controller.ProyectoC_controller import ProyectoC_controller
from service.Proyecto_C_service import Proyecto_C_service

from view.Elemento_view import Elemento_view
from controller.Elemento_controller import Elemento_controller
from service.Elemento_service import Elemento_service

from view.Laboratorio_view import Laboratorio_view
from controller.Laboratorio_controller import Laboratorio_controller
from service.Laboratorio_service import Laboratorio_service

from service.Estado_service import Estado_service

import sys
from PyQt5.QtWidgets import QApplication
from view.ExcelDrop_view import ExcelDropView
from controller.ExcelController import ExcelController

class Index_view:
    def __init__(self, root):
        self.root = root
        
        # 1. 창 크기 및 중앙 배치 (이전 가이드 적용)
        width, height = 600, 400
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.root.title("Laboratorio ciencias básicas UD")

        # 2. 메인 프레임 (expand=True를 주어 창 전체의 중앙에 오게 함)
        frame_btn = tk.Frame(root)
        frame_btn.pack(expand=True) 

        # 공통 버튼 스타일 설정
        btn_opt = {"width": 18, "pady": 5, "relief": "raised", "cursor": "hand2"}

        # 3. 버튼 생성 (기존 방식 유지하되 옵션만 추가)
        self.equipo_btn = tk.Button(frame_btn, text="Equipos", **btn_opt)
        self.equipo_btn.grid(row=0, column=0, padx=10, pady=10)

        self.listar_prestamo_btn = tk.Button(frame_btn, text="Listar prestamos", **btn_opt)
        self.listar_prestamo_btn.grid(row=0, column=1, padx=10, pady=10)

        self.estudiante_btn = tk.Button(frame_btn, text="Estudiantes", **btn_opt)
        self.estudiante_btn.grid(row=0, column=2, padx=10, pady=10)

        self.proyecto_c_btn = tk.Button(frame_btn, text="Proyecto curricular", **btn_opt)
        self.proyecto_c_btn.grid(row=1, column=0, padx=10, pady=10)

        self.elemento_btn = tk.Button(frame_btn, text="Elemento", **btn_opt)
        self.elemento_btn.grid(row=1, column=1, padx=10, pady=10)

        self.laboratorio_btn = tk.Button(frame_btn, text="Laboratorio", **btn_opt)
        self.laboratorio_btn.grid(row=1, column=2, padx=10, pady=10)

        self.excel_btn = tk.Button(frame_btn, text="Excel", **btn_opt)
        self.excel_btn.grid(row=2, column=0, padx=10, pady=10)

        # 4. 커맨드 연결 (기존 유지)
        self.equipo_btn.config(command=self.abrir_equipo_view)
        self.listar_prestamo_btn.config(command=self.abrir_listar_prestamo_view)
        self.estudiante_btn.config(command=self.abrir_estudiante_view)
        self.proyecto_c_btn.config(command=self.abrir_proyecto_c_view)
        self.elemento_btn.config(command=self.abrir_elemento_view)
        self.laboratorio_btn.config(command=self.abrir_laboratorio_view)
        self.excel_btn.config(command=self.abrir_excel_view)

    def abrir_equipo_view(self):
        # 새 창 생성
        ventana = tk.Toplevel(self.root)
        ventana.title("Modulo de equipo")

        ventana.lift()
        ventana.focus_force()
        self.root.bind("<FocusIn>", lambda e: self._ensure_top(ventana), add="+")
        
        # RegistrarEquipo_view 인스턴스 생성
        equipo_service = Equipo_service()
        equipo_view = Equipo_view(ventana)
        Equipo_controller(equipo_service, equipo_view)

    def abrir_listar_prestamo_view(self):
        # 새 창 생성
        ventana = tk.Toplevel(self.root)
        ventana.title("Modulo de listar prestamos")

        ventana.lift()
        ventana.focus_force()
        self.root.bind("<FocusIn>", lambda e: self._ensure_top(ventana), add="+")

        prestamo_service = Prestamo_service()
        consumible_service = Consumible_service()
        view = List_prestamo_view(ventana)
        List_prestamo_controller(prestamo_service,consumible_service, view)
    
    def abrir_estudiante_view(self):
        # 새 창 생성
        ventana = tk.Toplevel(self.root)
        ventana.title("Modulo de estudiante")

        ventana.lift()
        ventana.focus_force()
        self.root.bind("<FocusIn>", lambda e: self._ensure_top(ventana), add="+")

        # RegistrarEquipo_view 인스턴스 생성
        estudiante_service = Estudiante_service()
        prestamo_service = Prestamo_service()
        proyecto_service = Proyecto_C_service()
        estudiante_view = Estudiante_view(ventana)
        Estudiante_controller(estudiante_service,prestamo_service,proyecto_service,estudiante_view)

    def abrir_proyecto_c_view(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Modulo de proyecto curricular")

        ventana.lift()
        ventana.focus_force()
        self.root.bind("<FocusIn>", lambda e: self._ensure_top(ventana), add="+")

        proyecto_service = Proyecto_C_service()
        proyecto_view = ProyectoC_view(ventana)
        ProyectoC_controller(proyecto_service,proyecto_view)

    def abrir_elemento_view(self):
        # 1. 부모를 지정하여 생성 (계층 구조 유지)
        ventana = tk.Toplevel(self.root)
        ventana.title("Modulo de elemento")

        ventana.lift()
        ventana.focus_force()
        self.root.bind("<FocusIn>", lambda e: self._ensure_top(ventana), add="+")

        elemento_service = Elemento_service()
        elemento_view = Elemento_view(ventana)
        Elemento_controller(elemento_service, elemento_view)

    def abrir_laboratorio_view(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Modulo de laboratorio")

        ventana.lift()
        ventana.focus_force()
        self.root.bind("<FocusIn>", lambda e: self._ensure_top(ventana), add="+")

        laboratorio_service = Laboratorio_service()
        laboratorio_view = Laboratorio_view(ventana)
        Laboratorio_controller(laboratorio_service, laboratorio_view)
        
    def abrir_excel_view(self):
        app = QApplication(sys.argv)
        
        laboratorio_service = Laboratorio_service()
        elemento_service = Elemento_service()
        estado_service = Estado_service()
        equipo_service = Equipo_service()
        view = ExcelDropView()
        ExcelController(view,
                        elemento_service=elemento_service,
                        laboratorio_service=laboratorio_service,
                        estado_service=estado_service,
                        equipo_service=equipo_service)
        
        view.show()
        sys.exit(app.exec_())

    def _ensure_top(self, child): # 이 코드가 transient의 '항상 위에 있음' 기능을 대신합니다.
        if child.winfo_exists():
            child.lift()