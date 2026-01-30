from model.EstudianteDTO import EstudianteDTO
from model.EquipoDTO import EquipoDTO

class PrestamoDTO:
    def __init__(self, idPrestamo=0, fecha_inicio="", fecha_final="",multa = 0, estudiante = None, equipo = None):
        self.idPrestamo = idPrestamo
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        self.multa = multa
        self.estudiante = estudiante
        self.equipo = equipo

    # --- Getters ---
    def get_idPrestamo(self):
        return self.idPrestamo

    def get_fecha_inicio(self):
        return self.fecha_inicio

    def get_fecha_final(self):
        return self.fecha_final

    def get_multa(self):
        return self.multa

    def get_estudiante(self):
        return self.estudiante

    def get_equipo(self):
        return self.equipo

    # --- Setters ---
    def set_idPrestamo(self, idPrestamo):
        self.idPrestamo = idPrestamo

    def set_fecha_inicio(self, fecha_inicio):
        self.fecha_inicio = fecha_inicio

    def set_fecha_final(self, fecha_final):
        self.fecha_final = fecha_final

    def set_multa(self, multa):
        self.multa = multa

    def set_estudiante(self, estudiante: EstudianteDTO):
        self.estudiante = estudiante

    def set_equipo(self, equipo: EquipoDTO):
        self.equipo = equipo