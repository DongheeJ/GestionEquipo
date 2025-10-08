class EstudianteDAO:
    @staticmethod
    def listar():
        return "select e.idEstudiante,e.nombre,e.apellido,e.correo,e.celular,e.codigo,e.cedula, " \
        "pc.idProyecto_C, pc.nombre " \
        "from Estudiante e Join Proyecto_C pc " \
        "on (pc.idProyecto_C = e.idProyecto_C)"