from service.Estudiante_service import Estudiante_service
from service.Equipo_service import Equipo_service

class Prestamo_controller:
    def __init__(self, service, view):
        self.service = service
        self.view = view

        # 버튼 이벤트 연결
        view.btn_registrar.config(command=self.registrar)
        # view.btn_guardar.config(command=self.guardar)
    def registrar(self):
        placa = self.view.get_placa()
        inf_Estudiante = self.view.get_inf_Estudiante()
        equipo_service = Equipo_service()
        estudiante_service = Estudiante_service()
        equipo = equipo_service.seleccionar(placa)
        estudiante = estudiante_service.seleccionar(inf_Estudiante)
        self.service.registrar(hora_inicio,multa,estudiante.get_idEstudiante(),equipo.get_idEquipo())
        self.listar()  # 갱신