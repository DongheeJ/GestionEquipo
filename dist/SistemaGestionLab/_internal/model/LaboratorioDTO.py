class LaboratorioDTO:
    def __init__(self, idLaboratorio=0, nombre=""):
        self.idLaboratorio = idLaboratorio
        self.nombre = nombre
        

    # --- Getters ---
    def get_idLaboratorio(self):
        return self.idLaboratorio

    def get_nombre(self):
        return self.nombre

    # --- Setters ---
    def set_idLaboratorio(self, idLaboratorio):
        self.idLaboratorio = idLaboratorio

    def set_nombre(self, nombre):
        self.nombre = nombre