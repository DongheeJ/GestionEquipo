from persistencia.Conexion import get_conn
from persistencia.Elemento_DAO import Elemento_DAO as DAO
from model.ElementoDTO import ElementoDTO
from typing import List

class Elemento_service:
    def __init__(self):
        pass

    def listar(self,descripcion="") -> List[ElementoDTO]: 
        conn = get_conn()
        cur = conn.cursor()
        query,params = DAO.listar(descripcion)
        cur.execute(query,params)
        rs = cur.fetchall()

        elementos = []
        for r in rs:
            p = ElementoDTO(idElemento=r[0], descripcion=r[1],cantidad=r[2])
            elementos.append(p)

        cur.close()
        conn.close()
        return elementos

    def insertar(self,descripcion):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.insertar(descripcion))
        conn.commit()
        cur.close()
        conn.close()

    def delete(self,idElemento):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.delete(idElemento))
        conn.commit()
        cur.close()
        conn.close()

    def update(self,idElemento,descripcion):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.update(idElemento,descripcion))
        conn.commit()
        cur.close()
        conn.close()
