class LaboratorioDTO:
    def __init__(self, idLaboratorio=0, descripcion=""):
        self.idLaboratorio = idLaboratorio
        self.descripcion = descripcion
        

    # --- Getters ---
    def get_idLaboratorio(self):
        return self.idLaboratorio

    def get_descripcion(self):
        return self.descripcion

    # --- Setters ---
    def set_idLaboratorio(self, idLaboratorio):
        self.idLaboratorio = idLaboratorio

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion