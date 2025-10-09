from persistencia.Conexion import get_conn
from persistencia.Prestamo_DAO import Prestamo_DAO as DAO
from model.PrestamoDTO import PrestamoDTO

class Prestamo_service:
    def __init__(self):
        pass

    def es_prestamo_entregado(self,placa,inf_estudiante): 
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.es_prestamo_entregado(placa,inf_estudiante))
        ultimo = cur.fetchone()

        cur.close()
        conn.close()
        if (ultimo is None) or (ultimo[0] is not None):
            return True
        else:
            return False
    
    def registrar(hora_inicio,multa,idEstudiante,idEquipo):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.registrar(hora_inicio,multa,idEstudiante,idEquipo))
        conn.commit()
        cur.close()
        conn.close()