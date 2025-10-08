from model.LaboratorioDTO import LaboratorioDTO
from model.EstadoDTO import EstadoDTO
from model.ElementoDTO import ElementoDTO

class EquipoDTO:
    def __init__(self, idEquipo=0, placa="", Elemento=None, Laboratorio=None, Estado=None):
        self.idEquipo = idEquipo
        self.placa = placa
        self.Elemento = Elemento
        self.Laboratorio = Laboratorio
        self.Estado = Estado

    # Getters
    def get_idEquipo(self):
        return self.idEquipo

    def get_placa(self):
        return self.placa

    def get_Elemento(self):
        return self.Elemento

    def get_Laboratorio(self):
        return self.Laboratorio

    def get_Estado(self):
        return self.Estado

    # Setters
    def set_idEquipo(self, v):
        self.idEquipo = v

    def set_placa(self, v):
        self.placa = v

    def set_Elemento(self, v):
        if v is None or isinstance(v, ElementoDTO):
            self.Elemento = v
        else:
            raise TypeError("Elemento debe ser una instancia de ElementoDTO o None")

    def set_Laboratorio(self, v):
        if v is None or isinstance(v, LaboratorioDTO):
            self.Laboratorio = v
        else:
            raise TypeError("Laboratorio debe ser una instancia de LaboratorioDTO o None")

    def set_Estado(self, v):
        if v is None or isinstance(v, EstadoDTO):
            self.Estado = v
        else:
            raise TypeError("Estado debe ser una instancia de EstadoDTO o None")
