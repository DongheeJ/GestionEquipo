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
        
        cur.close()
        conn.close()
        return estudiantes

    def seleccionar(inf_estudiante):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.seleccionar(inf_estudiante))
        selected = cur.fetchone()

        cur.close()
        conn.close()
        
        pr = Proyecto_C_DTO(selected[7], selected[8])
        return EstudianteDTO(selected[0], selected[1], selected[2], selected[3], selected[4], selected[5], selected[6], pr)