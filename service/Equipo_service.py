from persistencia.Conexion import get_conn
from persistencia.EquipoDAO import EquipoDAO as DAO
from model.EquipoDTO import EquipoDTO
from model.EstadoDTO import EstadoDTO
from model.LaboratorioDTO import LaboratorioDTO
from model.ElementoDTO import ElementoDTO
class Equipo_service:
    def __init__(self):
        pass

    def listar(self): 
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.listar())
        rs = cur.fetchall()

        equipos = []
        for r in rs:
            el = ElementoDTO(idElemento=r[2], descripcion=r[3], cantidad=r[4])
            l = LaboratorioDTO(idLaboratorio=r[5], descripcion=r[6])
            es = EstadoDTO(idEstado=r[7], descripcion=r[8])
            eq = EquipoDTO(idEquipo=r[0], placa=r[1], Elemento=el, Laboratorio=l, Estado=es)

            equipos.append(eq)

        conn.close()
        return equipos
    
