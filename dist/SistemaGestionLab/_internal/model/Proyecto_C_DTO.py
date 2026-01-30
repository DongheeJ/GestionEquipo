class Proyecto_C_DTO:
    def __init__(self, idProyecto_C, nombre: str = ""):
        # Asigna pasando por los setters (aplican validación/normalización)
        self.idProyecto_C = idProyecto_C
        self.nombre = nombre
    # --- Getters ---
    def get_idProyecto_C(self):
        return self.idProyecto_C

    def get_nombre(self):
        return self.nombre

    # --- Setters ---
    def set_idProyecto_C(self, idProyecto_C):
        self.idProyecto_C = idProyecto_C

    def set_nombre(self, nombre: str):
        self.nombre = nombre