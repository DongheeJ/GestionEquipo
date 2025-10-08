from model.Proyecto_C_DTO import Proyecto_C_DTO

class EstudianteDTO:
    def __init__(self, idEstudiante, nombre="", apellido="", correo="", celular="", codigo="", cedula="", proyecto_c=None):
        self.idEstudiante = idEstudiante
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo  # 이메일은 소문자로 통일하려면 set_correo 사용
        self.celular = celular if celular else None
        self.codigo = codigo
        self.cedula = cedula
        self.proyecto_c = proyecto_c

    # getters
    def get_idEstudiante(self):
        return self.idEstudiante

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_correo(self):
        return self.correo

    def get_celular(self):
        return self.celular

    def get_codigo(self):
        return self.codigo

    def get_cedula(self):
        return self.cedula

    def get_proyecto_c(self):
        return self.proyecto_c

    # setters
    def set_idEstudiante(self, v):
        self.idEstudiante = v

    def set_nombre(self, v):
        self.nombre = v

    def set_apellido(self, v):
        self.apellido = v

    def set_correo(self, v):
        # 주석대로 소문자 통일하고 싶으면 아래 한 줄 유지
        self.correo = v.lower() if isinstance(v, str) else v

    def set_celular(self, v):
        self.celular = v if v else None

    def set_codigo(self, v):
        self.codigo = v

    def set_cedula(self, v):
        self.cedula = v

    def set_proyecto_c(self, v):
        if v is None or isinstance(v, Proyecto_C_DTO):
            self.proyecto_c = v
        else:
            raise TypeError("proyecto_c debe ser Proyecto_C_DTO o None")
