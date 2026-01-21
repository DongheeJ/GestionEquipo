# view/Prestamo_form_view.py
import tkinter as tk
from tkinter import ttk

class EditarPrestamo_view:
    def __init__(self, root):
        self.root = root
        width, height = 300, 300
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.root.title("Editar préstamo")

        frame = tk.Frame(root, padx=10, pady=10)
        frame.pack(fill="both", expand=True)

        # ===== Variables =====
        self.id_prestamo_var   = tk.StringVar()
        self.hora_inicio_var   = tk.StringVar()
        self.hora_final_var    = tk.StringVar()
        self.multa_var         = tk.StringVar()
        self.estudiante_var = tk.StringVar()
        self.equipo_var     = tk.StringVar()

        # ===== Campos =====
        # idPrestamo (normalmente solo lectura)
        tk.Label(frame, text="ID préstamo:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        entry_id = tk.Entry(frame, textvariable=self.id_prestamo_var, width=30)
        entry_id.grid(row=0, column=1, padx=5, pady=5)
        entry_id.configure(state="readonly")   # si quieres permitir edición, quita esta línea

        tk.Label(frame, text="Hora inicio (HH:MM):").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(frame, textvariable=self.hora_inicio_var, width=30).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="Hora final (HH:MM):").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(frame, textvariable=self.hora_final_var, width=30).grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame, text="Multa:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(frame, textvariable=self.multa_var, width=30).grid(row=3, column=1, padx=5, pady=5)

        tk.Label(frame, text="Estudiante:").grid(row=4, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(frame, textvariable=self.estudiante_var, width=30).grid(row=4, column=1, padx=5, pady=5)

        tk.Label(frame, text="Equipo:").grid(row=5, column=0, sticky="e", padx=5, pady=5)
        tk.Entry(frame, textvariable=self.equipo_var, width=30).grid(row=5, column=1, padx=5, pady=5)

        # ===== Botones =====
        btn_frame = tk.Frame(frame)
        btn_frame.grid(row=6, column=0, columnspan=2, pady=10)

        self.btn_editar = tk.Button(btn_frame, text="Guardar cambios")
        self.btn_editar.grid(row=0, column=0, padx=5)

        self.btn_cancelar = tk.Button(btn_frame, text="Cancelar")
        self.btn_cancelar.grid(row=0, column=1, padx=5)

    # ---- Obtener datos del formulario ----
    def get_datos(self):
        return {
            "idPrestamo":   self.id_prestamo_var.get().strip(),
            "hora_inicio":  self.hora_inicio_var.get().strip(),
            "hora_final":   self.hora_final_var.get().strip(),
            "multa":        self.multa_var.get().strip(),
            "estudiante": self.estudiante_var.get().strip(),
            "equipo":     self.estudiante_var.get().strip(),
        }

    # ---- Rellenar el formulario con datos existentes ----
    def set_datos(self, datos):
        self.id_prestamo_var.set(datos.get("idPrestamo", ""))
        self.hora_inicio_var.set(datos.get("hora_inicio", ""))
        self.hora_final_var.set(datos.get("hora_final", ""))
        self.multa_var.set(str(datos.get("multa", "")))
        self.estudiante_var.set(str(datos.get("estudiante", "")))
        self.equipo_var.set(str(datos.get("equipo", "")))
