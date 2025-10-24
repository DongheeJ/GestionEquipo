from persistencia.Conexion import get_conn
from persistencia.Prestamo_DAO import Prestamo_DAO as DAO
from model.PrestamoDTO import PrestamoDTO

class Prestamo_service:
    def __init__(self):
        pass

    def es_prestamo_libre(self,idEquipo): 
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.es_prestamo_libre(idEquipo))
        ultimo = cur.fetchone()

        cur.close()
        conn.close()
        if (ultimo is None) or (ultimo[0] is not None):
            return True
        else:
            return False
    
    def registrar(self,hora_inicio,multa,idEstudiante,idEquipo):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.registrar(hora_inicio,multa,idEstudiante,idEquipo))
        conn.commit()
        cur.close()
        conn.close()
    
    def seleccionar_ultimo(self,idEstudiante,idEquipo):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.seleccionar_ultimo(idEstudiante,idEquipo))
        f = cur.fetchone()

        cur.close()
        conn.close()
        if f is None:
            return None
        return PrestamoDTO(f[0],f[1],f[2],f[3])
    
    def entregar(self,hora_final,multa,idPrestamo):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.entregar(hora_final,multa,idPrestamo))
        conn.commit()
        cur.close()
        conn.close()