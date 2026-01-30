# service
from service.Laboratorio_service import Laboratorio_service
# view
from view.EditarLaboratorio_view import EditarLaboratorio_view
# model
from model.LaboratorioDTO import LaboratorioDTO

class EditarLaboratorio_controller:
    def __init__(
        self,
        service: Laboratorio_service,
        view: EditarLaboratorio_view,
        laboratorio: LaboratorioDTO,                 # int(id) 또는 laboratorio_C_DTO 둘 다 허용
        on_success=None           # 성공 후 콜백 함수(예: self.listar)
    ):
        self.service = service
        self.view = view
        self.on_success = on_success


        self.laboratorio = laboratorio

        if not self.laboratorio:
            self.view.mostrar_error("Error", "No se encontró el laboratorio.")
            return

        # 버튼 이벤트 연결
        self.view.btn_editar.config(command=self.editar)

        # 초기값 세팅
        self.view.set_datos({
            "nombre": self.laboratorio.get_nombre() or "",
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
        
        self.service.update(self.laboratorio.get_idLaboratorio(), nombre)

        self.view.mostrar_mensaje("OK", "El cambio se guardó correctamente.")

        # 성공 후: 목록 새로고침 + 창 닫기
        if callable(self.on_success):
            self.on_success()

        self.view.root.destroy()

    def cerrar(self):
        self.view.root.destroy()