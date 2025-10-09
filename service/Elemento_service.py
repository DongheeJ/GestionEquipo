from persistencia.Conexion import get_conn
from persistencia.Elemento_DAO import Elemento_DAO as DAO
from model.ElementoDTO import ElementoDTO

class Elemento_service:
    def __init__(self):
        pass

    def listar(self): 
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.listar())
        rs = cur.fetchall()

        elementos = []
        for r in rs:
            p = ElementoDTO(idElemento=r[0], descripcion=r[1], cantidad=r[2])
            elementos.append(p)

        cur.close()
        conn.close()
        return elementos