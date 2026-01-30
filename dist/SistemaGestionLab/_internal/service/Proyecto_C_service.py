from persistencia.Conexion import get_conn
from persistencia.Proyecto_C_DAO import Proyecto_C_DAO as DAO
from model.Proyecto_C_DTO import Proyecto_C_DTO
from typing import List

class Proyecto_C_service:
    def __init__(self):
        pass

    def listar(self,nombre="") -> List[Proyecto_C_DTO]: 
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.listar(nombre.strip()))
        rs = cur.fetchall()

        proyectos = []
        for r in rs:
            p = Proyecto_C_DTO(idProyecto_C=r[0], nombre=r[1])
            proyectos.append(p)

        cur.close()
        conn.close()
        return proyectos
    
    def insertar(self,nombre=""):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.insertar(nombre.strip()))
        conn.commit()
        cur.close()
        conn.close()

    def delete(self,id_proyecto):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.delete(id_proyecto))
        conn.commit()
        cur.close()
        conn.close()

    def update(self,id_proyecto,nombre=""):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.update(id_proyecto,nombre.strip()))
        conn.commit()
        cur.close()
        conn.close()
