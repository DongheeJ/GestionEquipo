import tkinter as tk
from tkinter import messagebox
from view.RegistrarEquipo_view import RegistrarEquipo_view
from controller.RegistrarEquipo_controller import RegistrarEquipo_controller
from service.Elemento_service import Elemento_service
from service.Laboratorio_service import Laboratorio_service
from service.Estado_service import Estado_service
from service.Equipo_service import Equipo_service

from view.Equipo_view import Equipo_view
from view.EditarEquipo_view import EditarEquipo_view
from controller.EditarEquipo_controller import EditarEquipo_controller

from model.EquipoDTO import EquipoDTO

class Equipo_controller:
    def __init__(self, service: Equipo_service, equipo_view: Equipo_view):
        self.service = service
        self.elemento_service = Elemento_service()
        self.laboratorio_service = Laboratorio_service()
        self.estado_service = Estado_service()
        self.equipo_view = equipo_view
        self.cargar_comboboxes()
        # 버튼 이벤트 연결
        self.equipo_view.btn_eliminar_multi.config(command=self.eliminar_multi)
        self.equipo_view.btn_listar.config(command=self.listar)
        self.equipo_view.btn_aplicar_filtros.config(command=self.aplicar_filtros)
        self.equipo_view.set_editar_handler(self.editar)
        self.equipo_view.set_eliminar_handler(self.eliminar)
        self.equipo_view.btn_registrar.config(command=self.abrir_registrar)

        self.listar()

    def listar(self):
        equipos = self.service.listar()  # DB → DTO
        self.equipo_view.mostrar_tabla(equipos)   # 테이블 표시

    def cargar_comboboxes(self):
        elementos = self.elemento_service.listar()
        datos_elem = [(e.get_idElemento(), e.get_descripcion()) for e in elementos]
        self.equipo_view.cargar_elementos(datos_elem)

        labs = self.laboratorio_service.listar()
        datos_lab = [(l.get_idLaboratorio(), l.get_nombre()) for l in labs]
        self.equipo_view.cargar_laboratorios(datos_lab)

    def aplicar_filtros(self):
        placa = self.equipo_view.get_placa()
        laboratorio = self.equipo_view.get_laboratorio()
        elemento = self.equipo_view.get_elemento()
        estado = self.equipo_view.get_filtros_estado()

        equipos = self.service.listar(
            placa=placa,
            estado=estado,
            laboratorio=laboratorio,
            elemento=elemento,
        )
        self.equipo_view.mostrar_tabla(equipos)

    def editar(self,equipo,elemento_desc,laboratorio_nombre):
        win = tk.Toplevel(self.equipo_view.root)
        win.title("Editar equipo")
        win.grab_set()

        form_view = EditarEquipo_view(win)

        EditarEquipo_controller(
            equipo_service=self.service,      # 기존 estudiante_service 대응
            form_view=form_view,
            equipo=equipo,                   # 기존 estudiante 대응 (EquipoDTO)
            elemento_desc=elemento_desc,               # ElementoDTO 객체
            laboratorio_nombre=laboratorio_nombre,         # LaboratorioDTO 객체
            on_success=self.listar     # 성공 시 목록 새로고침 콜백
        )

    def abrir_registrar(self):
        # 새 창 생성
        win = tk.Toplevel(self.equipo_view.root)
        win.title("Registrar equipo")
        win.grab_set()

        # RegistrarEquipo_view 인스턴스 생성
        registrar_view = RegistrarEquipo_view(win)

        # RegistrarEquipo_controller 도 연결 (필요하면)
        RegistrarEquipo_controller(self.service, self.elemento_service, self.laboratorio_service, registrar_view,self.listar)

    def eliminar(self, equipo: EquipoDTO,estado):
        confirmar = messagebox.askyesno(
            "Confirmar",
            f"¿Seguro que deseas eliminar el equipo (placa: {equipo.get_placa()})?"
        )
        if not confirmar:
            return
        if estado == "en uso":
            messagebox.showerror("Error", f"Es un equipo que está en uso.")
            return

        try:
            self.service.delete(equipo.get_idEquipo())
            messagebox.showinfo("OK", "equipo eliminado correctamente.")
            self.listar()  
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar.\n{e}")

    def eliminar_multi(self):
        # id가 문자열로 올 수도 있어서 int 변환
        confirmar = messagebox.askyesno(
            "Confirmar",
            f"¿Seguro que deseas eliminar los equipos?"
        )
        if not confirmar:
            return

        try:
            ids = self.equipo_view.get_selected_ids()
            for id in ids:
                self.service.delete(id)
                # print(id)

            messagebox.showinfo("OK", "Equipos eliminados correctamente.")
            self.listar()  
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar.\n{e}")