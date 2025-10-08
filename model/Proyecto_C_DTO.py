class Proyecto_C_DTO:
    def __init__(self, idProyecto_C, nombre: str = ""):
        # Asigna pasando por los setters (aplican validación/normalización)
        self.idProyecto_C = idProyecto_C
        self.nombre = nombre

    # --- idProyecto_C ---
    @property
    def idProyecto_C(self):
        return self._idProyecto_C

    @idProyecto_C.setter
    def idProyecto_C(self, value):
        if value is not None and not isinstance(value, int):
            raise TypeError("idProyecto_C debe ser int o None")
        self._idProyecto_C = value

    # --- nombre ---
    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str):
        v = "" if value is None else str(value).strip()
        self._nombre = v

    def __repr__(self) -> str:
        return f"Proyecto_C_DTO(idProyecto_C={self.idProyecto_C}, nombre='{self.nombre}')"
