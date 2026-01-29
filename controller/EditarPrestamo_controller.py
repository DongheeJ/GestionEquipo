import tkinter as tk
from tkinter import messagebox
# model
from model.PrestamoDTO import PrestamoDTO
# service
from service.Prestamo_service import Prestamo_service
# view
from view.EditarPrestamo_view import EditarPrestamo_view

class EditarPrestamo_controller:
    def __init__(self, prestamo_service: Prestamo_service, form_view: EditarPrestamo_view, prestamo: PrestamoDTO, on_success=None):

        self.prestamo_service = prestamo_service
        self.view = form_view
        self.on_success = on_success
        self.prestamo = prestamo

        # ----- 폼에 기존 데이터 세팅 -----
        self.view.set_datos({
            "idPrestamo":   self.prestamo.get_idPrestamo(),
            "fecha_inicio":  self.prestamo.get_fecha_inicio(),
            "fecha_final":   self.prestamo.get_fecha_final(),
            "multa":        self.prestamo.get_multa(),
            "estudiante": self.prestamo.get_estudiante().get_nombre(),
            "equipo":     self.prestamo.get_equipo().get_Elemento().get_descripcion()+"-"+self.prestamo.get_equipo().get_placa()
        })

        # ----- 버튼 핸들러 연결 -----
        self.view.btn_editar.config(command=self.editar)
        self.view.btn_cancelar.config(command=self.cerrar)

    # ================== 액션들 ==================

    def editar(self):
        datos = self.view.get_datos()
        root = self.view.root   # Toplevel 윈도우

        # 필수값 검증 (원하는 필드만 골라서)
        if not datos["fecha_inicio"] or not datos["fecha_final"]:
            messagebox.showwarning(
                "Datos incompletos",
                "Hora de inicio y hora final son obligatorias.",
                parent=root,
            )
            return

        # ---- 타입 변환 (문자열 → 숫자) ----
        multa = None
        if datos["multa"]:
            try:
                multa = float(datos["multa"])
            except ValueError:
                messagebox.showwarning(
                    "Valor inválido",
                    "La multa debe ser un número.",
                    parent=root,
                )
                return

        id_estudiante = None
        if datos["idEstudiante"]:
            try:
                id_estudiante = int(datos["idEstudiante"])
            except ValueError:
                messagebox.showwarning(
                    "Valor inválido",
                    "ID de estudiante debe ser un número entero.",
                    parent=root,
                )
                return

        id_equipo = None
        if datos["idEquipo"]:
            try:
                id_equipo = int(datos["idEquipo"])
            except ValueError:
                messagebox.showwarning(
                    "Valor inválido",
                    "ID de equipo debe ser un número entero.",
                    parent=root,
                )
                return

        try:
            # 🔹 Prestamo_service 의 editar 시그니처에 맞게 이름만 맞추면 됨
            self.prestamo_service.editar(
                idPrestamo=self.prestamo.get_idPrestamo(),
                fecha_inicio=datos["fecha_inicio"],
                fecha_final=datos["fecha_final"],
                multa=multa,
                idEstudiante=id_estudiante,
                idEquipo=id_equipo,
            )

            messagebox.showinfo(
                "Éxito",
                "Préstamo modificado correctamente.",
                parent=root,
            )

            # 메인 리스트 새로고침 콜백
            if self.on_success:
                self.on_success()

            self.cerrar()

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Ocurrió un error al modificar el préstamo:\n{e}",
                parent=root,
            )

    def cerrar(self):
        self.view.root.destroy()