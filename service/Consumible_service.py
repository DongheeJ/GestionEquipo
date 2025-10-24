from persistencia.Conexion import get_conn
from persistencia.Consumible_DAO import Consumible_DAO as DAO
from model.ConsumibleDTO import ConsumibleDTO

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