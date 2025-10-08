class ElementoDTO:
    def __init__(self, idElemento=0, descripcion="",cantidad=0):
        self.idElemento = idElemento
        self.descripcion = descripcion
        self.cantidad = cantidad

    # Getters
    def get_idElemento(self):
        return self.idElemento

    def get_descripcion(self):
        return self.descripcion
    
    def get_cantidad(self):
        return self.cantidad

    # Setters
    def set_idElemento(self, idElemento):
        self.idElemento = idElemento

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion
    
    def set_cantidad(self, cantidad):
        self.cantidad = cantidad
