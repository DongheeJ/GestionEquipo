import tkinter as tk
from tkinter import ttk
from service.Equipo_service import Equipo_service

from view.Equipo_view import Equipo_view
from controller.Equipo_controller import Equipo_controller

from service.Prestamo_service import Prestamo_service
from service.Consumible_service import Consumible_service
from service.Estudiante_service import Estudiante_service

from controller.Prestamo_controller import List_prestamo_controller
from view.Prestamo_view import List_prestamo_view

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

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Laboratorio")
        self.root.state('zoomed') # 메인 창 전체화면

        # 1. 탭 컨트롤(Notebook) 생성
        self.tabControl = ttk.Notebook(self.root)
        self.tabControl.pack(expand=1, fill="both")

        # 2. 각 모듈을 위한 프레임(탭) 생성
        self.tab_prestamo = ttk.Frame(self.tabControl)
        self.tab_equipo = ttk.Frame(self.tabControl)
        self.tab_elemento = ttk.Frame(self.tabControl)
        self.tab_estudiante = ttk.Frame(self.tabControl)
        self.tab_proyecto = ttk.Frame(self.tabControl)
        self.tab_laboratorio = ttk.Frame(self.tabControl)
        self.tab_excel = ttk.Frame(self.tabControl)
        # 3. 탭 추가
        self.tabControl.add(self.tab_prestamo, text='Préstamo')
        self.tabControl.add(self.tab_equipo, text='Equipo')
        self.tabControl.add(self.tab_elemento, text='Elemento')
        self.tabControl.add(self.tab_estudiante, text='Estudiante')
        self.tabControl.add(self.tab_proyecto, text='Proyecto')
        self.tabControl.add(self.tab_laboratorio, text='Laboratorio')
        self.tabControl.add(self.tab_excel, text='Importar Excel') # Excel 탭 추가

        self.tabControl.pack(expand=1, fill="both")
        self.setup_all_tabs()

    def setup_all_tabs(self):
        """모든 탭을 초기화하고 컨트롤러를 연결합니다."""
        self.setup_prestamo_tab()
        self.setup_equipo_tab()
        self.setup_elemento_tab()
        self.setup_estudiante_tab()
        self.setup_proyecto_tab()
        self.setup_laboratorio_tab()
        self.setup_excel_tab()

    def setup_equipo_tab(self):
        equipo_service = Equipo_service()
        equipo_view = Equipo_view(self.tab_equipo) 
        Equipo_controller(equipo_service, equipo_view)

    def setup_prestamo_tab(self):
        prestamo_service = Prestamo_service()
        consumible_service = Consumible_service()
        view = List_prestamo_view(self.tab_prestamo)
        List_prestamo_controller(prestamo_service, consumible_service, view)

    def setup_estudiante_tab(self):
        estudiante_service = Estudiante_service()
        prestamo_service = Prestamo_service()
        proyecto_service = Proyecto_C_service()
        # 부모를 self.tab_estudiante 프레임으로 설정
        estudiante_view = Estudiante_view(self.tab_estudiante)
        Estudiante_controller(estudiante_service, prestamo_service, proyecto_service, estudiante_view)

    def setup_proyecto_tab(self):
        proyecto_service = Proyecto_C_service()
        # 부모를 self.tab_proyecto 프레임으로 설정
        proyecto_view = ProyectoC_view(self.tab_proyecto)
        ProyectoC_controller(proyecto_service, proyecto_view)

    def setup_elemento_tab(self):
        elemento_service = Elemento_service()
        # 부모를 self.tab_elemento 프레임으로 설정
        elemento_view = Elemento_view(self.tab_elemento)
        Elemento_controller(elemento_service, elemento_view)

    def setup_laboratorio_tab(self):
        laboratorio_service = Laboratorio_service()
        # 부모를 self.tab_laboratorio 프레임으로 설정
        laboratorio_view = Laboratorio_view(self.tab_laboratorio)
        Laboratorio_controller(laboratorio_service, laboratorio_view)

    def setup_excel_tab(self):
        """Excel 탭은 프레임 안에 버튼을 두어 기존 PyQt5 창을 실행하도록 합니다."""
        label = tk.Label(self.tab_excel, text="Módulo de Importación de Inventario", font=("Arial", 12))
        label.pack(pady=20)
        
        btn_importar = tk.Button(
            self.tab_excel, 
            text="Abrir Herramienta de Importación (Excel)", 
            command=self.abrir_excel_view, # 기존 창 열기 메서드 활용

        )
        btn_importar.pack(pady=10)

    def abrir_excel_view(self):
        # 1. 이미 QApplication 인스턴스가 있는지 확인 (중복 생성 방지)
        app = QApplication.instance()
        if not app:
            app = QApplication(sys.argv)
        
        laboratorio_service = Laboratorio_service()
        elemento_service = Elemento_service()
        estado_service = Estado_service()
        equipo_service = Equipo_service()
        
        # 2. View 생성 및 컨트롤러 연결
        view = ExcelDropView()
        ExcelController(view,
                        elemento_service=elemento_service,
                        laboratorio_service=laboratorio_service,
                        estado_service=estado_service,
                        equipo_service=equipo_service)
        
        view.show()

        # 3. sys.exit()를 빼고 exec_()만 실행합니다.
        # 이 루프가 끝나도 파이썬이 종료되지 않고 Tkinter로 제어권이 돌아갑니다.
        app.exec_()