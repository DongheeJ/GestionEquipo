# service
from service.Elemento_service import Elemento_service
# view
from view.EditarElemento_view import EditarElemento_view
# model
from model.ElementoDTO import ElementoDTO

class EditarElemento_controller:
    def __init__(
        self,
        service: Elemento_service,
        view: EditarElemento_view,
        elemento: ElementoDTO,                 # int(id) 또는 Proyecto_C_DTO 둘 다 허용
        on_success=None           # 성공 후 콜백 함수(예: self.listar)
    ):
        self.service = service
        self.view = view
        self.on_success = on_success

        self.elemento = elemento

        if not self.elemento:
            self.view.mostrar_error("Error", "No se encontró el elemento.")
            return

        # 버튼 이벤트 연결
        self.view.btn_editar.config(command=self.editar)

        # 초기값 세팅
        self.view.set_datos({
            "descripcion": self.elemento.get_descripcion() or ""
        })

    def editar(self):
        descripcion = self.view.get_descripcion().strip()
        
        if not descripcion:
            self.view.mostrar_error("Error", "Todos los campos son obligatorios.")
            return

        confirmacion = self.view.confirmar("Confirmación de registro",
                                        "¿Está seguro de que desea registrar estos datos?")

        if not confirmacion:
            return
        
        self.service.update(self.elemento.get_idElemento(), descripcion)

        self.view.mostrar_mensaje("OK", "El cambio se guardó correctamente.")

        # 성공 후: 목록 새로고침 + 창 닫기
        if callable(self.on_success):
            self.on_success()

        self.view.root.destroy()

    def cerrar(self):
        self.view.root.destroy()