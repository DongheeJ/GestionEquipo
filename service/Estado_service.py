from persistencia.Conexion import get_conn
from persistencia.Estado_DAO import Estado_DAO as DAO
from model.EstadoDTO import EstadoDTO

class Estado_service:
    def __init__(self):
        pass

    def listar(self): 
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.listar())
        rs = cur.fetchall()

        estados = []
        for r in rs:
            p = EstadoDTO(idEstado=r[0], descripcion=r[1])
            estados.append(p)

        conn.close()
        return estados