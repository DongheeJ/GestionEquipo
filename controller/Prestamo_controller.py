from datetime import datetime
from tkinter import messagebox
# service
from service.Prestamo_service import Prestamo_service
from service.Estudiante_service import Estudiante_service
from service.Equipo_service import Equipo_service
from service.Consumible_service import Consumible_service

from view.Prestamo_view import Prestamo_view

class Prestamo_controller:
    def __init__(self, service: Prestamo_service, view: Prestamo_view, 
                estudiante_service: Estudiante_service, equipo_service: Equipo_service,
                consumible_service: Consumible_service, on_success=None):
        self.service = service
        self.view = view
        self.estudiante_service = estudiante_service
        self.equipo_service = equipo_service
        self.consumible_service = consumible_service
        self.on_success = on_success
        # 버튼 이벤트 연결
        self.view.btn_registrar.config(command=self.registrar)
        self.view.btn_entregar.config(command=self.entregar)
        self.view.btn_clear.config(command=self.view.clear)

    def registrar(self):
        placa = self.view.get_placa()
        inf_Estudiante = self.view.get_inf_Estudiante()
        consumibles = self.view.get_consumibles()
        equipo_service = self.equipo_service
        estudiante_service = self.estudiante_service
        service = self.service

        hora_inicio = datetime.now().strftime("%Y-%m-%d %H:%M")
        multa_txt = self.view.get_multa()
        multa = "0"
        estudiante = estudiante_service.seleccionar(inf_Estudiante)
        equipo = equipo_service.seleccionar(placa)

        if estudiante is None:
            messagebox.showerror("Alerta", "No se encontró los datos del estudiante")
            return
        if equipo is None:
            messagebox.showerror("Alerta", "No se encontró los datos del equipo")
            return
        if not service.es_prestamo_libre(equipo.get_idEquipo()):
            messagebox.showerror("Alerta", "Es un equipo que NO está libre")
            return
        
        messagebox.showinfo("Registro exitoso","Prestamo registrado de manera exitosa")
        self.service.registrar(hora_inicio,multa,estudiante.get_idEstudiante(),equipo.get_idEquipo())
        prestamo = service.seleccionar_ultimo(estudiante.get_idEstudiante(),equipo.get_idEquipo())
        if consumibles:
            consumibles = [c for c in consumibles if c.strip() != ""]
            self.consumible_service.registrar(consumibles,prestamo.get_idPrestamo())
        equipo_service.actualizar_estado(equipo.get_idEquipo(),idEstado = 2)
        self.view.clear()
        if self.on_success:
            self.on_success()

    def entregar(self):
        placa = self.view.get_placa()
        inf_Estudiante = self.view.get_inf_Estudiante()
        equipo_service = self.equipo_service
        estudiante_service = self.estudiante_service
        service = self.service

        hora_final = datetime.now().strftime("%Y-%m-%d %H:%M")
        multa_txt = self.view.get_multa()
        multa = multa_txt if multa_txt else "0"
        estudiante = estudiante_service.seleccionar(inf_Estudiante)
        equipo = equipo_service.seleccionar(placa)
        if estudiante is None:
            messagebox.showerror("Alerta", "No se encontró los datos del estudiante")
            return
        if equipo is None:
            messagebox.showerror("Alerta", "No se encontró los datos del equipo")
            return
        prestamo = service.seleccionar_ultimo(estudiante.get_idEstudiante(),equipo.get_idEquipo())
        if prestamo is None:
            messagebox.showinfo("", "El equipo no pertenece al préstamo actual de este estudiante.")
            return
        messagebox.showinfo("Entrega exitosa","Equipo entregado de manera exitosa")
        self.service.entregar(hora_final,multa,prestamo.get_idPrestamo())
        equipo_service.actualizar_estado(equipo.get_idEquipo(),idEstado = 1)
        self.view.clear()
        if self.on_success:
            self.on_success()