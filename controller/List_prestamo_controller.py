# view
from view.Prestamo_view import Prestamo_view
from view.List_prestamo_view import List_prestamo_view

# model
from model.PrestamoDTO import PrestamoDTO
# service
from service.Equipo_service import Equipo_service
from service.Estudiante_service import Estudiante_service
from service.Prestamo_service import Prestamo_service
from service.Consumible_service import Consumible_service
# controller
from controller.Prestamo_controller import Prestamo_controller

from tkinter import Toplevel, Listbox, END, messagebox, simpledialog
import tkinter as tk

from datetime import datetime
from tkinter import messagebox

class List_prestamo_controller:
    def __init__(self, prestamo_service: Prestamo_service,
                consumible_service: Consumible_service, 
                view: List_prestamo_view, 
                estudiante="", multados=False, no_entregados=False, on_success=None):
        self.prestamo_service = prestamo_service
        self.consumible_service = consumible_service
        self.equipo_service = Equipo_service()
        self.estudiante_service = Estudiante_service()
        self.view = view
        self.view.btn_eliminar_multi.config(command=self.eliminar_multi)
        self.view.set_ver_consumibles_handler(self.ver_consumibles)
        self.view.set_pagar_multa_handle(self.pagar_multa)
        self.view.set_entregar_handle(self.entregar)
        self.view.set_eliminar_handle(self.eliminar)

        self.estudiante = estudiante
        self.multados = multados
        self.no_entregados = no_entregados
        self.on_success = on_success

        self.view.btn_aplicar_filtros.config(
            command=self.aplicar_filtros
        )
        # aplica todos los filtros seleccionados
        self.view.btn_listar_todos.config(
            command=self.listar
        )
        self.view.btn_registrar.config(
            command=self.abrir_registrar
        )
        # 처음에는 아무 필터 없이 전체 목록
        self.aplicar_filtros()

    def centrar_ventana(self,win,parent):
        win.update_idletasks()

        width = win.winfo_width()
        height = win.winfo_height()

        parent_x = parent.winfo_x()
        parent_y = parent.winfo_y()
        parent_width = parent.winfo_width()
        parent_height = parent.winfo_height()

        x = parent_x + (parent_width // 2) - (width // 2)
        y = parent_y + (parent_height // 2) - (height // 2)

        win.geometry(f"+{x}+{y}")

    def ver_consumibles(self, prestamo: PrestamoDTO):
        consumibles = self.consumible_service.listar_por_prestamo(
            prestamo.get_idPrestamo()
        )

        win = Toplevel(self.view.root)
        win.title(f"Consumibles del préstamo {prestamo.get_idPrestamo()}")

        lb = Listbox(win, width=50)
        lb.pack(padx=10, pady=10)

        if not consumibles:
            lb.insert(END, "(Sin consumibles)")
        else:
            for c in consumibles:
                texto = f"{c.get_idConsumible()} - {c.get_descripcion()}"
                lb.insert(END, texto)

        # 🔽 여기서 가운데 정렬
        self.centrar_ventana(win, self.view.root)

    def aplicar_filtros(self):
        # 1) 체크박스 상태 읽기

        # 2) estudiante / equipo 텍스트 읽기
        if self.estudiante != "":
            self.view.set_estudiante(self.estudiante)
            self.estudiante = ""
        if self.multados:
            self.view.set_multados(self.multados)
            self.multados = False
        if self.no_entregados:
            self.view.set_no_entregados(self.no_entregados)
            self.no_entregados = False

        estudiante = self.view.get_estudiante()
        equipo = self.view.get_placa()
        multados = self.view.get_multados()
        no_entregados = self.view.get_no_entregados()
        entregados = self.view.get_entregados()
        sort_fecha = self.view.get_sort_field()
        sort_order = self.view.get_sort_order()
        # 3) service에서 PrestamoDTO 리스트 받아오기
        prestamos = self.prestamo_service.listar(
            estudiante=estudiante,
            equipo=equipo,
            multados=multados,
            no_entregados=no_entregados,
            entregados=entregados,
            sort_fecha=sort_fecha,
            sort_order=sort_order
        )

        # 4) prestamos 객체 그대로 전달
        self.view.render(prestamos)

    def listar(self):
        prestamos = self.prestamo_service.listar()
        self.view.render(prestamos)
    
    def abrir_registrar(self):
        ventana = tk.Toplevel()
        ventana.title("Mantenimiento de prestamos")
    
        view = Prestamo_view(ventana)
        prestamo_service = self.prestamo_service
        estudiante_service = Estudiante_service()
        equipo_service = Equipo_service()
        consumible_service = self.consumible_service

        Prestamo_controller(
            prestamo_service, view,
            estudiante_service,
            equipo_service,
            consumible_service,
            self.listar
        )
    def cobrar_multa(self):
        multa = 0
        multa_str = simpledialog.askstring(
            "Pagar multa",
            f"¿Cuánto debe?",
            parent=self.view.root if hasattr(self, "view") else None
        )
        if multa_str is None:
            return 0

        try:
            multa = float(multa_str.replace(",", ".").strip())
        except ValueError:
            messagebox.showwarning("Valor inválido", "Por favor ingresa un número válido.")
            return 0

        if multa <= 0:
            messagebox.showwarning("Valor inválido", "El monto debe ser mayor que 0.")
            return 0
        confirmar = messagebox.askyesno(
            "Cobrar multa",
            f"¿Confirmas el valor?"
        )
        if not confirmar: 
            return 0
        return multa
    
    def entregar(self, prestamo: PrestamoDTO):
        if prestamo.get_fecha_final() is not None:
            messagebox.showerror("","El prestamo ya está entregado.")
            return
        
        multa = 0
        
        while multa == 0:
            cobrar_multa = messagebox.askyesno(
                "Entregar equipo",
                f"¿El estudiante debe una multa?"
            )
            if not cobrar_multa:
                break
            if cobrar_multa:
                multa = self.cobrar_multa()

        confirmar = messagebox.askyesno(
            "Entregar equipo",
            f"El valor de la multa: {multa}\n¿Confirmas la entrega?"
        )
        if not confirmar:
            return
        
        fecha_final = datetime.now().strftime("%Y-%m-%d %H:%M")
        equipo = prestamo.get_equipo()

        messagebox.showinfo("Entrega exitosa","Equipo entregado de manera exitosa")
        self.prestamo_service.entregar(fecha_final,multa,prestamo.get_idPrestamo())
        self.equipo_service.actualizar_estado(equipo.get_idEquipo(),idEstado = 1)
        self.listar()

    def pagar_multa(self, prestamo: PrestamoDTO):
        id_prestamo = prestamo.get_idPrestamo()
        
        multa_actual = prestamo.get_multa() or 0
        try:
            multa_actual = float(multa_actual)
        except Exception:
            multa_actual = 0

        if multa_actual <= 0:
            messagebox.showinfo("Sin multa", f"El préstamo #{id_prestamo} no tiene multa pendiente.")
            return

        # ✅ (추가) 전액 결제 옵션 먼저
        pagar_todo = messagebox.askyesno(
            "Pagar multa",
            f"Multa pendiente: {multa_actual}\n\n¿Quieres pagar TODO ahora?"
        )

        if pagar_todo:
            monto = multa_actual
        else:
            # 1) 금액 입력
            monto_str = simpledialog.askstring(
                "Pagar multa",
                f"Multa pendiente: {multa_actual}\n¿Cuánto quieres pagar?",
                parent=self.view.root if hasattr(self, "view") else None
            )
            if monto_str is None:
                return  # 취소

            # 2) 입력값 검증
            try:
                monto = float(monto_str.replace(",", ".").strip())
            except ValueError:
                messagebox.showwarning("Valor inválido", "Por favor ingresa un número válido.")
                return

            if monto <= 0:
                messagebox.showwarning("Valor inválido", "El monto debe ser mayor que 0.")
                return

            if monto > multa_actual:
                messagebox.showwarning(
                    "Monto excedido",
                    f"El monto ({monto}) no puede ser mayor que la multa pendiente ({multa_actual})."
                )
                return

        # 3) 최종 확인
        resp = messagebox.askyesno(
            "Confirmar pago",
            f"Vas a pagar {monto} de una multa pendiente de {multa_actual}.\n¿Confirmas?",
        )
        if not resp:
            return

        # 4) 서비스 호출
        try:
            self.prestamo_service.pagar_multa(id_prestamo, monto)

            pendiente = multa_actual - monto
            messagebox.showinfo(
                "Éxito",
                f"Pago registrado: {monto}.\nPendiente: {pendiente}"
            )

            self.listar()

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar el pago:\n{e}")

    def eliminar(self, prestamo: PrestamoDTO):
        confirmar = messagebox.askyesno(
            "Confirmar",
            f"¿Seguro que deseas eliminar el prestamo (ID: {prestamo.get_idPrestamo()})?"
        )
        if not confirmar:
            return

        try:
            self.prestamo_service.delete(prestamo.get_idPrestamo())
            messagebox.showinfo("OK", "prestamo eliminado correctamente.")
            self.listar()  
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar.\n{e}")

    def eliminar_multi(self):
        # id가 문자열로 올 수도 있어서 int 변환
        confirmar = messagebox.askyesno(
            "Confirmar",
            f"¿Seguro que deseas eliminar los prestamos?"
        )
        if not confirmar:
            return

        try:
            id_prestamos = self.view.get_selected_ids()
            for id in id_prestamos:
                self.prestamo_service.delete(id)

            messagebox.showinfo("OK", "Prestamo eliminado correctamente.")
            self.listar()  
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar.\n{e}")