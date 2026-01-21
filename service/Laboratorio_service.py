from persistencia.Conexion import get_conn
from persistencia.Laboratorio_DAO import Laboratorio_DAO as DAO
from model.LaboratorioDTO import LaboratorioDTO
from typing import List

class Laboratorio_service:
    def __init__(self):
        pass

    def listar(self,nombre="") -> List[LaboratorioDTO]: 
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.listar(nombre))
        rs = cur.fetchall()

        laboratorios = []
        for r in rs:
            p = LaboratorioDTO(idLaboratorio=r[0], nombre=r[1])
            laboratorios.append(p)

        cur.close()
        conn.close()
        return laboratorios

    def insertar(self,nombre):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.insertar(nombre))
        conn.commit()
        cur.close()
        conn.close()

    def delete(self,idLaboratorio):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.delete(idLaboratorio))
        conn.commit()
        cur.close()
        conn.close()

    def update(self,idLaboratorio,nombre):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.update(idLaboratorio,nombre))
        conn.commit()
        cur.close()
        conn.close()
