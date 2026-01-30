# service
from service.Proyecto_C_service import Proyecto_C_service
# view
from view.EditarProyectoC_view import EditarProyectoC_view
# model
from model.Proyecto_C_DTO import Proyecto_C_DTO

class EditarProyectoC_controller:
    def __init__(
        self,
        service: Proyecto_C_service,
        view: EditarProyectoC_view,
        proyecto: Proyecto_C_DTO,                 # int(id) 또는 Proyecto_C_DTO 둘 다 허용
        on_success=None           # 성공 후 콜백 함수(예: self.listar)
    ):
        self.service = service
        self.view = view
        self.on_success = on_success


        self.proyecto = proyecto

        if not self.proyecto:
            self.view.mostrar_error("Error", "No se encontró el proyecto.")
            return

        # 버튼 이벤트 연결
        self.view.btn_editar.config(command=self.editar)

        # 초기값 세팅
        self.view.set_datos({
            "nombre": self.proyecto.get_nombre() or "",
        })

    def editar(self):
        nombre = self.view.get_nombre().strip()

        if not nombre:
            self.view.mostrar_error("Error", "El nombre es obligatorio.")
            return

        confirmacion = self.view.confirmar("Confirmación de registro",
                                        "¿Está seguro de que desea registrar estos datos?")

        if not confirmacion:
            return
        
        self.service.update(self.proyecto.get_idProyecto_C(), nombre)

        self.view.mostrar_mensaje("OK", "El cambio se guardó correctamente.")

        # 성공 후: 목록 새로고침 + 창 닫기
        if callable(self.on_success):
            self.on_success()

        self.view.root.destroy()

    def cerrar(self):
        self.view.root.destroy()