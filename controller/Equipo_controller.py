class Equipo_controller:
    def __init__(self, service, view):
        self.service = service
        self.view = view

        # 버튼 이벤트 연결
        view.btn_listar.config(command=self.listar)
        # view.btn_guardar.config(command=self.guardar)

    def listar(self):
        equipos = self.service.listar()  # DB → DTO
        datos = [(e.idEquipo, e.placa) for e in equipos]
        self.view.mostrar_tabla(datos)   # 테이블 표시

    # def guardar(self):
    #     placa = self.view.get_placa()
    #     nuevo = EquipoDTO(placa=placa)
    #     self.service.crear(nuevo)
    #     self.listar()  # 갱신