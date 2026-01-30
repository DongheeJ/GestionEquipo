import tkinter as tk
from tkinter import messagebox

from service.Equipo_service import Equipo_service
from view.EditarEquipo_view import EditarEquipo_view

from service.Elemento_service import Elemento_service
from service.Laboratorio_service import Laboratorio_service

from model.EquipoDTO import EquipoDTO


class EditarEquipo_controller:
    def __init__(self, equipo_service: Equipo_service,
                form_view: EditarEquipo_view,
                equipo: EquipoDTO, 
                elemento_desc, 
                laboratorio_nombre, 
                on_success=None):

        self.equipo_service = equipo_service
        self.view = form_view
        self.on_success = on_success  # 수정/등록 성공 후 목록 새로고침을 위한 콜백
        
        # 주입받은 DTO 객체들 저장
        self.equipo = equipo
        self.elemento_desc = elemento_desc
        self.laboratorio_nombre = laboratorio_nombre

        self.view.set_datos({
            "placa": self.equipo.get_placa(),
            "elemento_desc": self.elemento_desc if self.elemento_desc else "",
            "laboratorio_nombre": self.laboratorio_nombre if self.laboratorio_nombre else ""
        })

        # ----- elementos 목록 로드 -----
        elemento_service = Elemento_service()
        elementos = elemento_service.listar()

        self.elemento_to_id = {
            e.get_descripcion(): e.get_idElemento() for e in elementos
        }
        opciones = list(self.elemento_to_id.keys())
        self.view.set_elementos(opciones)

        # ----- laboratorios 목록 로드 -----
        laboratorio_service = Laboratorio_service()
        laboratorios = laboratorio_service.listar()

        self.lab_to_id = {
            l.get_nombre(): l.get_idLaboratorio() for l in laboratorios
        }
        opciones = list(self.lab_to_id.keys())
        self.view.set_laboratorios(opciones)

        # ----- 버튼 핸들러 연결 -----
        self.view.btn_editar.config(command=self.editar)
        self.view.btn_cancelar.config(command=self.cerrar)

    # ================== 액션들 ==================

    def editar(self):
        datos = self.view.get_datos()
        root = self.view.root   # Toplevel 윈도우

        idElemento = None
        if datos["elemento_desc"]:
            idElemento = self.elemento_to_id.get(datos["elemento_desc"])

        idLaboratorio = None
        if datos["laboratorio_nombre"]:
            idLaboratorio = self.lab_to_id.get(datos["laboratorio_nombre"])

        confirmacion = messagebox.askyesno("Confirmación de registro",
                                        "¿Está seguro de que desea registrar estos datos?")
        # service를 통해 DB insert
        if not confirmacion:
            return
        
        title, message = self.equipo_service.editar(
            idEquipo=self.equipo.get_idEquipo(),
            placa = datos["placa"],
            idElemento=idElemento,
            idLaboratorio=idLaboratorio
        )
        if title == "OK":
            messagebox.showinfo(
                title,
                message,
                parent=root,
            )
            # 메인 리스트 새로고침 콜백
            if self.on_success:
                self.on_success()
            self.cerrar()
        else:
            messagebox.showerror(
                title,
                message,
                parent=root,
            )

    def cerrar(self):
        self.view.root.destroy()