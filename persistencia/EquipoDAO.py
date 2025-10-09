class EquipoDAO:
    @staticmethod
    def listar():
        return "select e.idEquipo,e.placa,el.idElemento,el.descripcion,el.cantidad,l.idLaboratorio,l.nombre,es.idEstado,es.descripcion " \
        "from Equipo e Join Elemento el on (e.idElemento = el.idElemento)" \
        "join Laboratorio l  on (e.idLaboratorio = l.idLaboratorio)" \
        "join Estado es  on (e.idEstado = es.idEstado)" 

    def seleccionar(placa):
        return "select e.idEquipo,e.placa,el.idElemento,el.descripcion,el.cantidad,l.idLaboratorio,l.nombre,es.idEstado,es.descripcion " \
        "from Equipo e Join Elemento el on (e.idElemento = el.idElemento)" \
        "join Laboratorio l  on (e.idLaboratorio = l.idLaboratorio)" \
        "join Estado es  on (e.idEstado = es.idEstado)" \
        "where e.placa = {placa}" 