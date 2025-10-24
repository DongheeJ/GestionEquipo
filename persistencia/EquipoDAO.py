class EquipoDAO:
    @staticmethod
    def listar():
        return "select e.idEquipo,e.placa,el.idElemento,el.descripcion,el.cantidad,l.idLaboratorio,l.nombre,es.idEstado,es.descripcion " \
        "from Equipo e Join Elemento el on (e.idElemento = el.idElemento)" \
        "join Laboratorio l  on (e.idLaboratorio = l.idLaboratorio)" \
        "join Estado es  on (e.idEstado = es.idEstado)" 

    def seleccionar(placa):
        return (
            f"SELECT e.idEquipo, e.placa, el.idElemento, el.descripcion, el.cantidad, "
            f"l.idLaboratorio, l.nombre, es.idEstado, es.descripcion "
            f"FROM Equipo e "
            f"JOIN Elemento el ON (e.idElemento = el.idElemento) "
            f"JOIN Laboratorio l ON (e.idLaboratorio = l.idLaboratorio) "
            f"JOIN Estado es ON (e.idEstado = es.idEstado) "
            f"WHERE e.placa = '{placa}'"
        )