from persistencia.Conexion import get_conn
from persistencia.Consumible_DAO import Consumible_DAO as DAO
from model.ConsumibleDTO import ConsumibleDTO
from model.PrestamoDTO import PrestamoDTO
from service.Prestamo_service import Prestamo_service
from typing import List

class Consumible_service:
    def __init__(self):
        pass

    def registrar(self,consumibles = [], idPrestamo = 0):
        conn = get_conn()
        cur = conn.cursor()
        for c in consumibles:
            cur.execute(DAO.registrar(c,idPrestamo))
        
        conn.commit()
        cur.close()
        conn.close()

    def listar_por_prestamo(self,idPrestamo) -> List[ConsumibleDTO]: 
        pService = Prestamo_service()
        prestamos = pService.mapear()

        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.listar_por_prestamo(idPrestamo))
        rs = cur.fetchall()

        consumibles = []
        for r in rs:
            p = prestamos[r[2]]
            c = ConsumibleDTO(r[0], r[1], p)
            consumibles.append(c)

        cur.close()
        conn.close()
        return consumibles

    # def listar(self): 
    #     conn = get_conn()
    #     cur = conn.cursor()
    #     cur.execute(DAO.listar())
    #     rs = cur.fetchall()

    #     consumibles = []
    #     for r in rs:
    #         c = ConsumibleDTO(idElemento=r[0], descripcion=r[1], cantidad=r[2])
    #         consumibles.append(c)

    #     cur.close()
    #     conn.close()
    #     return consumibles