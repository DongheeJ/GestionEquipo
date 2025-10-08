from model.EstudianteDTO import EstudianteDTO
from model.EquipoDTO import EquipoDTO

class PrestamoDTO:
    def __init__(self, idPrestamo=0, hora_inicio="", hora_final="",multa = 0, estudiante = None, equipo = None):
        self.idPrestamo = idPrestamo
        self.hora_inicio = hora_inicio
        self.hora_final = hora_final
        self.multa = multa
        self.estudiante = estudiante
        self.equipo = equipo

    # --- Getters ---
    def get_idPrestamo(self):
        return self.idPrestamo

    def get_hora_inicio(self):
        return self.hora_inicio

    def get_hora_final(self):
        return self.hora_final

    def get_multa(self):
        return self.multa

    def get_estudiante(self):
        return self.estudiante

    def get_equipo(self):
        return self.equipo

    # --- Setters ---
    def set_idPrestamo(self, idPrestamo):
        self.idPrestamo = idPrestamo

    def set_hora_inicio(self, hora_inicio):
        self.hora_inicio = hora_inicio

    def set_hora_final(self, hora_final):
        self.hora_final = hora_final

    def set_multa(self, multa):
        self.multa = multa

    def set_estudiante(self, estudiante: EstudianteDTO):
        self.estudiante = estudiante

    def set_equipo(self, equipo: EquipoDTO):
        self.equipo = equipo