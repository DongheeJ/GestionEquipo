import tkinter as tk
from tkinter import messagebox
from view.RegistrarElemento_view import RegistrarElemento_view
from controller.RegistrarElemento_controller import RegistrarElemento_controller

from service.Elemento_service import Elemento_service
from view.Elemento_view import Elemento_view
from model.ElementoDTO import ElementoDTO

from view.EditarElemento_view import EditarElemento_view
from controller.EditarElemento_controller import EditarElemento_controller

class Elemento_controller:
    def __init__(self, service: Elemento_service, view: Elemento_view):
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
        elementos: list[ElementoDTO] = self.service.listar()
        self.view.mostrar_tabla(elementos)

    def aplicar_filtros(self):
        descripcion = self.view.get_filtro_desc()
        elementos: list[ElementoDTO] = self.service.listar(descripcion)
        self.view.mostrar_tabla(elementos)

    def abrir_registrar(self):
        ventana = tk.Toplevel(self.view.root)
        ventana.title("Registrar elemento")

        ventana.transient(self.view.root) # Elemento_view 위에 고정
        ventana.lift() # 창을 맨 위로 올림
        ventana.focus_force()
        ventana.grab_set()                # 이 창을 닫기 전까지 부모 창 클릭 불가 (모달)

        registrar_view = RegistrarElemento_view(ventana)
        RegistrarElemento_controller(self.service, registrar_view,self.listar)

    def abrir_editar(self,elemento: ElementoDTO):
        win = tk.Toplevel(self.view.root)
        win.title("Editar elemento")

        win.transient(self.view.root) # Elemento_view 위에 고정
        win.lift() # 창을 맨 위로 올림
        win.focus_force()
        win.grab_set()                # 이 창을 닫기 전까지 부모 창 클릭 불가 (모달)

        form_view = EditarElemento_view(win)

        EditarElemento_controller(self.service,form_view,elemento,self.listar)

    def eliminar(self, idElemento):
        # id가 문자열로 올 수도 있어서 int 변환
        try:
            idElemento = int(idElemento)
        except (TypeError, ValueError):
            messagebox.showerror("Error", "ID inválido.")
            return

        confirmar = messagebox.askyesno(
            "Confirmar",
            f"¿Seguro que deseas eliminar el proyecto (ID: {idElemento})?"
        )
        if not confirmar:
            return

        try:
            self.service.delete(idElemento)
            messagebox.showinfo("OK", "Elemento eliminado correctamente.")
            self.listar()  
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar.\n{e}")
