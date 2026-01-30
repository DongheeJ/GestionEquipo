# service
from service.Elemento_service import Elemento_service
# view
from view.RegistrarElemento_view import RegistrarElemento_view

class RegistrarElemento_controller:
    def __init__(self, service : Elemento_service, view : RegistrarElemento_view, on_success):
        self.service = service 
        self.view = view
        self.on_success = on_success
        # 버튼 이벤트 연결
        self.view.btn_registrar.config(command=self.registrar)

    def registrar(self):
        descripcion = self.view.get_descripcion()

        # 간단한 검증
        if not descripcion:
            self.view.mostrar_error("Error", "Todos los campos son obligatorios.")
            return

        confirmacion = self.view.confirmar("Confirmación de registro",
                                        "¿Está seguro de que desea registrar estos datos?")

        if not confirmacion:
            return
        
        # service를 통해 DB insert
        self.service.insertar(descripcion)

        self.view.mostrar_mensaje("OK", "Elemento registrado correctamente.")
        if callable(self.on_success):
            self.on_success()

        self.view.root.destroy()

    def cerrar(self):
        self.view.root.destroy()
