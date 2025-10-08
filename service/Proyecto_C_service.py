from persistencia.Conexion import get_conn
from persistencia.Proyecto_C_DAO import Proyecto_C_DAO as DAO
from model.Proyecto_C_DTO import Proyecto_C_DTO

class Proyecto_C_service:
    def __init__(self):
        pass

    def listar(self): 
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.listar())
        rs = cur.fetchall()

        proyectos = []
        for r in rs:
            p = Proyecto_C_DTO(idProyecto_C=r[0], nombre=r[1])
            proyectos.append(p)

        conn.close()
        return proyectos