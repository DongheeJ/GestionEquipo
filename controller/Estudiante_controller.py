from tkinter import messagebox
import tkinter as tk
from service.Consumible_service import Consumible_service
from view.List_prestamo_view import List_prestamo_view
from controller.List_prestamo_controller import List_prestamo_controller
from view.RegistrarEstudiante_view import RegistrarEstudiante_view
from view.EditarEstudiante_view import EditarEstudiante_view
from controller.RegistrarEstudiante_controller import RegistrarEstudiante_controller
from controller.EditarEstudiante_controller import EditarEstudiante_controller

from service.Estudiante_service import Estudiante_service
from view.Estudiante_view import Estudiante_view
from model.EstudianteDTO import EstudianteDTO

from service.Prestamo_service import Prestamo_service

from service.Proyecto_C_service import Proyecto_C_service

class Estudiante_controller:
    def __init__(self, estudiante_service: Estudiante_service, prestamo_service: Prestamo_service, proyecto_service: Proyecto_C_service, estidiante_view: Estudiante_view):
        self.estudiante_service = estudiante_service
        self.prestamo_service = prestamo_service
        self.proyecto_service = proyecto_service
        self.estidiante_view = estidiante_view

        self.estidiante_view.btn_eliminar_multi.config(command=self.eliminar_multi)
        self.estidiante_view.btn_listar.config(command=self.listar)
        self.estidiante_view.btn_aplicar_filtros.config(command=self.aplicar_filtros)
        self.estidiante_view.set_ver_prestamos_handler(self.ver_prestamos)
        self.estidiante_view.set_editar_handler(self.editar)
        self.estidiante_view.set_eliminar_handler(self.eliminar)

        self.estidiante_view.btn_registrar.config(command=self.abrir_form_registro)
        self.cargar_comboboxes()
        self.listar()

    def listar(self):
        estudiantes = self.estudiante_service.listar()
        self.estidiante_view.mostrar_tabla(estudiantes)

    def aplicar_filtros(self):
        inf = self.estidiante_view.get_busqueda_codigo_cedula()
        proyecto_c = self.estidiante_view.get_filtro_proyecto()
        multado = self.estidiante_view.get_filtro_multado()
        no_entregado = self.estidiante_view.get_filtro_no_entregado()

        estudiantes = self.estudiante_service.listar(
            inf=inf,
            proyecto_c=proyecto_c,
            multado=multado,
            no_entregado=no_entregado,
        )
        self.estidiante_view.mostrar_tabla(estudiantes)

    def ver_prestamos(self, estudiante,multados=False,no_entregados=False):
        ventana = tk.Toplevel()
        ventana.title("Modulo de listar prestamos")

        consumible_service = Consumible_service()
        view = List_prestamo_view(ventana)
        List_prestamo_controller(self.prestamo_service,consumible_service, view, estudiante,multados,no_entregados)

    def editar(self,estudiante,proyecto):
        win = tk.Toplevel(self.estidiante_view.root)
        win.title("Editar estudiante")
        win.grab_set()

        form_view = EditarEstudiante_view(win)

        EditarEstudiante_controller(
            estudiante_service=self.estudiante_service,
            form_view=form_view,
            estudiante=estudiante,
            proyecto=proyecto,
            on_success=self.listar,
        )

    def eliminar(self, estudiante: EstudianteDTO):
        confirmar = messagebox.askyesno(
            "Confirmar",
            f"¿Seguro que deseas eliminar el estudiante (Codigo: {estudiante.get_codigo()})?"
        )
        if not confirmar:
            return

        try:
            self.estudiante_service.delete(estudiante.get_idEstudiante())
            messagebox.showinfo("OK", "estudiante eliminado correctamente.")
            self.listar()  
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar.\n{e}")

    def abrir_form_registro(self):
        win = tk.Toplevel(self.estidiante_view.root)
        win.title("Registrar estudiante")
        win.grab_set()   

        form_view = RegistrarEstudiante_view(win)

        RegistrarEstudiante_controller(
            estudiante_service=self.estudiante_service,
            form_view=form_view,
            on_success=self.listar,
        )

    def cargar_comboboxes(self):
        proyectos = self.proyecto_service.listar()
        datos_elem = [(p.get_idProyecto_C(), p.get_nombre()) for p in proyectos]
        self.estidiante_view.cargar_proyectos(datos_elem)

    def eliminar_multi(self):
        # id가 문자열로 올 수도 있어서 int 변환
        confirmar = messagebox.askyesno(
            "Confirmar",
            f"¿Seguro que deseas eliminar los estudiantes?"
        )
        if not confirmar:
            return

        try:
            ids = self.estidiante_view.get_selected_ids()
            for id in ids:
                self.estudiante_service.delete(id)
                # print(id)

            messagebox.showinfo("OK", "Estudiantes eliminados correctamente.")
            self.listar()  
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar.\n{e}")