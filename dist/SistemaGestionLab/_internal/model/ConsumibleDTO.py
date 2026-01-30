class ConsumibleDTO:
    def __init__(self, idConsumible=0, descripcion="", prestamo=None):
        self.idConsumible = idConsumible
        self.descripcion = descripcion
        self.prestamo = prestamo

    # Getters
    def get_idConsumible(self):
        return self.idConsumible

    def get_descripcion(self):
        return self.descripcion
    
    def get_prestamo(self):
        return self.prestamo

    # Setters
    def set_idConsumible(self, idConsumible):
        self.idConsumible = idConsumible

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion
    
    def set_prestamo(self, prestamo):
        self.prestamo = prestamo
