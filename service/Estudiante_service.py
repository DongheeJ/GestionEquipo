from persistencia.Conexion import get_conn
from persistencia.EstudianteDAO import EstudianteDAO as DAO
from model.EstudianteDTO import EstudianteDTO
from model.Proyecto_C_DTO import Proyecto_C_DTO
class Estudiante_service:
    def __init__(self):
        pass
    def listar(self): 
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.listar())
        rs = cur.fetchall()

        estudiantes = []
        for r in rs:
            pr = Proyecto_C_DTO(r[7], r[8])
            e  = EstudianteDTO(r[0], r[1], r[2], r[3], r[4], r[5], r[6], pr)
            estudiantes.append(e)
        
        conn.close()
        return estudiantes