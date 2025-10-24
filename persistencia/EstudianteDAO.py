class EstudianteDAO:
    @staticmethod
    def listar():
        return "select e.idEstudiante,e.nombre,e.apellido,e.correo,e.celular,e.codigo,e.cedula, " \
        "pc.idProyecto_C, pc.nombre " \
        "from Estudiante e Join Proyecto_C pc " \
        "on (pc.idProyecto_C = e.idProyecto_C)"
    
    def seleccionar(inf_estudiante):
        return (
            f"SELECT e.idEstudiante, e.nombre, e.apellido, e.correo, e.celular, e.codigo, e.cedula, "
            f"pc.idProyecto_C, pc.nombre "
            f"FROM Estudiante e "
            f"JOIN Proyecto_C pc ON (pc.idProyecto_C = e.idProyecto_C) "
            f"WHERE (e.codigo = '{inf_estudiante}' OR e.cedula = '{inf_estudiante}')"
        )