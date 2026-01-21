import tkinter as tk
from tkinter import messagebox
from view.RegistrarProyectoC_view import RegistrarProyectoC_view
from controller.RegistrarProyectoC_controller import RegistrarProyectoC_controller

from service.Proyecto_C_service import Proyecto_C_service
from view.ProyectoC_view import ProyectoC_view
from model.Proyecto_C_DTO import Proyecto_C_DTO

from view.EditarProyectoC_view import EditarProyectoC_view
from controller.EditarProyectoC_controller import EditarProyectoC_controller

class ProyectoC_controller:
    def __init__(self, service: Proyecto_C_service, view: ProyectoC_view):
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
        proyectos: list[Proyecto_C_DTO] = self.service.listar()
        self.view.mostrar_tabla(proyectos)

    def aplicar_filtros(self):
        nombre = self.view.get_filtro_nombre()
        proyectos: list[Proyecto_C_DTO] = self.service.listar(nombre)
        self.view.mostrar_tabla(proyectos)

    def abrir_registrar(self):
        ventana = tk.Toplevel()
        ventana.title("Registrar proyecto curricular")

        ventana.transient(self.view.root) # Elemento_view 위에 고정
        ventana.lift() # 창을 맨 위로 올림
        ventana.focus_force()
        ventana.grab_set()                # 이 창을 닫기 전까지 부모 창 클릭 불가 (모달)

        registrar_view = RegistrarProyectoC_view(ventana)

        # RegistrarEquipo_controller 도 연결 (필요하면)
        RegistrarProyectoC_controller(self.service, registrar_view,self.listar)

    def abrir_editar(self,proyecto: Proyecto_C_DTO):
        win = tk.Toplevel(self.view.root)
        win.title("Editar proyecto curricular")

        win.transient(self.view.root) # Elemento_view 위에 고정
        win.lift() # 창을 맨 위로 올림
        win.focus_force()
        win.grab_set()                # 이 창을 닫기 전까지 부모 창 클릭 불가 (모달)
        
        form_view = EditarProyectoC_view(win)

        EditarProyectoC_controller(self.service,form_view,proyecto,self.listar)

    def eliminar(self, id_proyectoC):
        # id가 문자열로 올 수도 있어서 int 변환
        try:
            id_proyectoC = int(id_proyectoC)
        except (TypeError, ValueError):
            messagebox.showerror("Error", "ID inválido.")
            return

        confirmar = messagebox.askyesno(
            "Confirmar",
            f"¿Seguro que deseas eliminar el proyecto (ID: {id_proyectoC})?"
        )
        if not confirmar:
            return

        try:
            self.service.delete(id_proyectoC)
            messagebox.showinfo("OK", "Proyecto eliminado correctamente.")
            self.listar()  
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar.\n{e}")
