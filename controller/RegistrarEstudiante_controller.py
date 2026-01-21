import tkinter as tk
from tkinter import messagebox
from service.Proyecto_C_service import Proyecto_C_service

class RegistrarEstudiante_controller:
    def __init__(self, estudiante_service, form_view, on_success=None):
        self.estudiante_service = estudiante_service
        self.view = form_view
        self.on_success = on_success   # 예: listar_todos 같은 콜백

        # ----- Proyecto 목록 로드 -----
        proyecto_service = Proyecto_C_service()
        proyectos = proyecto_service.listar()   # [Proyecto_C_DTO, ...]

        self.nombre_to_id = {
            p.get_nombre(): p.get_idProyecto_C() for p in proyectos
        }
        opciones = list(self.nombre_to_id.keys())
        self.view.set_proyectos(opciones)

        # ----- 버튼 핸들러 연결 -----
        self.view.set_guardar_handler(self.guardar)
        self.view.set_cancelar_handler(self.cerrar)

    # ================== 액션들 ==================

    def guardar(self):
        datos = self.view.get_datos()
        root = self.view.root   # Toplevel 윈도우

        # 필수값 검증
        if not datos["nombre"] or not datos["apellido"] \
            or not datos["codigo"] or not datos["cedula"]:
            messagebox.showwarning(
                "Datos incompletos",
                "Nombre, apellido, código y cédula son obligatorios.",
                parent=root,
            )
            return

        id_proyecto = None
        if datos["proyecto_nombre"]:
            id_proyecto = self.nombre_to_id.get(datos["proyecto_nombre"])

        confirmacion = messagebox.askyesno("Confirmación de registro",
                                        "¿Está seguro de que desea registrar estos datos?")
        # service를 통해 DB insert
        if not confirmacion:
            return
        
        try:
            # 🔹 네 service 시그니처에 맞게 파라미터만 조정
            self.estudiante_service.registrar(
                nombre=datos["nombre"],
                apellido=datos["apellido"],
                correo=datos["correo"],
                celular=datos["celular"],
                codigo=datos["codigo"],
                cedula=datos["cedula"],
                idProyecto_C=id_proyecto,
            )
            messagebox.showinfo(
                "Éxito",
                "Estudiante registrado correctamente.",
                parent=root,
            )
            # 메인 리스트 새로고침 콜백
            if self.on_success:
                self.on_success()
            self.cerrar()
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Ocurrió un error al registrar:\n{e}",
                parent=root,
            )

    def cerrar(self):
        self.view.root.destroy()
