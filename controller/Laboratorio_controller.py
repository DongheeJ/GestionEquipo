import tkinter as tk
from tkinter import messagebox
from view.RegistrarLaboratorio_view import RegistrarLaboratorio_view
from controller.RegistrarLaboratorio_controller import RegistrarLaboratorio_controller

from service.Laboratorio_service import Laboratorio_service
from view.Laboratorio_view import Laboratorio_view
from model.LaboratorioDTO import LaboratorioDTO

from view.EditarLaboratorio_view import EditarLaboratorio_view
from controller.EditarLaboratorio_controller import EditarLaboratorio_controller

class Laboratorio_controller:
    def __init__(self, service: Laboratorio_service, view: Laboratorio_view):
        self.service = service
        self.view = view
        
        # 버튼 이벤트 연결
        self.view.btn_listar.config(command=self.listar)
        self.view.btn_aplicar_filtros.config(command=self.aplicar_filtros)
        self.view.btn_registrar.config(command=self.abrir_registrar)
        self.view.set_editar_handler(self.abrir_editar)
        self.view.set_eliminar_handler(self.eliminar)

        self.listar()
        
    def listar(self):
        laboratorios: list[LaboratorioDTO] = self.service.listar()
        self.view.mostrar_tabla(laboratorios)

    def aplicar_filtros(self):
        nombre = self.view.get_filtro_nombre()
        laboratorios: list[LaboratorioDTO] = self.service.listar(nombre)
        self.view.mostrar_tabla(laboratorios)

    def abrir_registrar(self):
        ventana = tk.Toplevel()
        ventana.title("Registrar laboratorio")

        ventana.transient(self.view.root) # Elemento_view 위에 고정
        ventana.lift() # 창을 맨 위로 올림
        ventana.focus_force()
        ventana.grab_set()                # 이 창을 닫기 전까지 부모 창 클릭 불가 (모달)

        registrar_view = RegistrarLaboratorio_view(ventana)

        # RegistrarEquipo_controller 도 연결 (필요하면)
        RegistrarLaboratorio_controller(self.service, registrar_view,self.listar)

    def abrir_editar(self,laboratorio: LaboratorioDTO):
        win = tk.Toplevel(self.view.root)
        win.title("Editar laboratorio")

        win.transient(self.view.root) # Elemento_view 위에 고정
        win.lift() # 창을 맨 위로 올림
        win.focus_force()
        win.grab_set()                # 이 창을 닫기 전까지 부모 창 클릭 불가 (모달)
        
        form_view = EditarLaboratorio_view(win)

        EditarLaboratorio_controller(self.service,form_view,laboratorio,self.listar)

    def eliminar(self, idLaboratorio):
        # id가 문자열로 올 수도 있어서 int 변환
        try:
            idLaboratorio = int(idLaboratorio)
        except (TypeError, ValueError):
            messagebox.showerror("Error", "ID inválido.")
            return

        confirmar = messagebox.askyesno(
            "Confirmar",
            f"¿Seguro que deseas eliminar el laboratorio (ID: {idLaboratorio})?"
        )
        if not confirmar:
            return

        try:
            self.service.delete(idLaboratorio)
            messagebox.showinfo("OK", "Laboratorio eliminado correctamente.")
            self.listar()  
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar.\n{e}")
