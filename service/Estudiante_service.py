from persistencia.Conexion import get_conn
from persistencia.EstudianteDAO import EstudianteDAO as DAO
from model.EstudianteDTO import EstudianteDTO
from model.Proyecto_C_DTO import Proyecto_C_DTO
from typing import List

class Estudiante_service:
    def __init__(self):
        pass
    
    def listar(self,inf = "", proyecto_c="", multado = False,no_entregado = False) -> List[EstudianteDTO]: 
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.listar(inf, proyecto_c, multado, no_entregado))
        rs = cur.fetchall()

        estudiantes = []
        for r in rs:
            pr = Proyecto_C_DTO(r[7], r[8])
            e  = EstudianteDTO(r[0], r[1], r[2], r[3], r[4], r[5], r[6], pr)
            estudiantes.append(e)
        
        cur.close()
        conn.close()
        return estudiantes

    def mapear(self,inf = "", proyecto_c="", multado = False,no_entregado = False) -> List[EstudianteDTO]: 
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.listar(inf, proyecto_c, multado, no_entregado))
        rs = cur.fetchall()

        estudiantes = {}
        for r in rs:
            pr = Proyecto_C_DTO(r[7], r[8])
            e  = EstudianteDTO(r[0], r[1], r[2], r[3], r[4], r[5], r[6], pr)
            estudiantes[r[0]] = e
        
        cur.close()
        conn.close()
        return estudiantes
    
    def seleccionar(self,inf_estudiante) -> EstudianteDTO:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.seleccionar(inf_estudiante))
        selected = cur.fetchone()

        cur.close()
        conn.close()
        
        if(selected is None):
            return None
        
        pr = Proyecto_C_DTO(selected[7], selected[8])
        return EstudianteDTO(selected[0], selected[1], selected[2], selected[3], selected[4], selected[5], selected[6], pr)
    
    def registrar(self,nombre="", apellido="", correo="", celular="", codigo="", cedula="", idProyecto_C=None):
        conn = get_conn()
        cur = conn.cursor()
        query, param = DAO.registrar(nombre, apellido, correo, celular, codigo, cedula, idProyecto_C)
        cur.execute(query,param)
        conn.commit()
        cur.close()
        conn.close()

    def editar(self,id,nombre="", apellido="", correo="", celular="", codigo="", cedula="", idProyecto_C=None):
        conn = get_conn()
        cur = conn.cursor()
        query, param = DAO.editar(id, nombre, apellido, correo, celular, codigo, cedula, idProyecto_C)
        cur.execute(query,param)
        conn.commit()
        cur.close()
        conn.close()

    def delete(self,idEstudiante):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.delete(idEstudiante))
        conn.commit()
        cur.close()
        conn.close()