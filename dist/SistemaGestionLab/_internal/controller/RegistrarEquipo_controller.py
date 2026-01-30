from view.RegistrarEquipo_view import RegistrarEquipo_view
from service.Equipo_service import Equipo_service
from service.Elemento_service import Elemento_service
from service.Laboratorio_service import Laboratorio_service

class RegistrarEquipo_controller:
    def __init__(self, service: Equipo_service, elemento_service: Elemento_service,
                laboratorio_service: Laboratorio_service, view: RegistrarEquipo_view,
                on_success=None):
        self.service = service
        self.elemento_service = elemento_service
        self.laboratorio_service = laboratorio_service
        self.view = view
        self.on_success = on_success
        # 콤보박스 데이터 로딩
        self.cargar_comboboxes()

        # 버튼 이벤트 연결
        self.view.btn_registrar.config(command=self.registrar)

    def cargar_comboboxes(self):
        elementos = self.elemento_service.listar()
        datos_elem = [(e.get_idElemento(), e.get_descripcion()) for e in elementos]
        self.view.cargar_elementos(datos_elem)

        labs = self.laboratorio_service.listar()
        datos_lab = [(l.get_idLaboratorio(), l.get_nombre()) for l in labs]
        self.view.cargar_laboratorios(datos_lab)

    def registrar(self):
        datos = self.view.get_datos_equipo()

        # 간단한 검증
        # if not datos["placa"] or not all([datos["idElemento"], datos["idLaboratorio"]]):
        #     self.view.mostrar_error("Error", "Todos los campos son obligatorios.")
        #     return

        confirmacion = self.view.confirmar(
            "Confirmación de registro",
            "¿Está seguro de que desea registrar estos datos?"
        )
        # service를 통해 DB insert
        if not confirmacion:
            return
        title,message = self.service.insertar(
            datos["placa"],
            datos["idElemento"],
            datos["idLaboratorio"],
        )
        if title == "ERROR":
            self.view.mostrar_error(title,message)
        else:
            self.view.mostrar_mensaje(title,message)
            if callable(self.on_success):
                self.on_success()
                self.view.root.destroy()
