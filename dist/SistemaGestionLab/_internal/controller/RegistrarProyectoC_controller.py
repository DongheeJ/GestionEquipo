# service
from service.Proyecto_C_service import Proyecto_C_service
# view
from view.RegistrarProyectoC_view import RegistrarProyectoC_view

class RegistrarProyectoC_controller:
    def __init__(self, service : Proyecto_C_service, view : RegistrarProyectoC_view, on_success):
        self.service = service 
        self.view = view
        self.on_success = on_success
        # 버튼 이벤트 연결
        self.view.btn_registrar.config(command=self.registrar)

    def registrar(self):
        nombre = self.view.get_nombre()

        # 간단한 검증
        if not nombre:
            self.view.mostrar_error("Error", "Todos los campos son obligatorios.")
            return

        confirmacion = self.view.confirmar("Confirmación de registro",
                                        "¿Está seguro de que desea registrar estos datos?")

        if not confirmacion:
            return
        # service를 통해 DB insert
        self.service.insertar(nombre)

        self.view.mostrar_mensaje("OK", "Proyecto registrado correctamente.")
        if callable(self.on_success):
            self.on_success()

        self.view.root.destroy()

    def cerrar(self):
        self.view.root.destroy()
