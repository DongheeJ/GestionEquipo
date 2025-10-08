class EstadoDTO:
    def __init__(self, idEstado=0, descripcion=""):
        self.idEstado = idEstado
        self.descripcion = descripcion

    # Getters
    def get_idEstado(self):
        return self.idEstado

    def get_descripcion(self):
        return self.descripcion

    # Setters
    def set_idEstado(self, idEstado):
        self.idEstado = idEstado

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion
