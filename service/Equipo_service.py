from persistencia.Conexion import get_conn
from persistencia.EquipoDAO import EquipoDAO as DAO
from model.EquipoDTO import EquipoDTO
from model.EstadoDTO import EstadoDTO
from model.LaboratorioDTO import LaboratorioDTO
from model.ElementoDTO import ElementoDTO
from typing import List
import sqlite3

class Equipo_service:
    def __init__(self):
        pass

    def listar(self,placa="", estado="", laboratorio="", elemento="") -> List[EquipoDTO]: 
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.listar(placa, estado, laboratorio, elemento))
        rs = cur.fetchall()

        equipos = []
        for r in rs:
            el = ElementoDTO(idElemento=r[2], descripcion=r[3])
            l = LaboratorioDTO(idLaboratorio=r[4], nombre=r[5])
            es = EstadoDTO(idEstado=r[6], descripcion=r[7])
            eq = EquipoDTO(idEquipo=r[0], placa=r[1], Elemento=el, Laboratorio=l, Estado=es)

            equipos.append(eq)

        cur.close()
        conn.close()
        return equipos

    def mapear(self,placa="", estado="", laboratorio="", elemento="")-> List[EquipoDTO]: 
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.listar(placa, estado, laboratorio, elemento))
        rs = cur.fetchall()
        equipos = {}
        for r in rs:
            el = ElementoDTO(idElemento=r[2], descripcion=r[3])
            l = LaboratorioDTO(idLaboratorio=r[4], nombre=r[5])
            es = EstadoDTO(idEstado=r[6], descripcion=r[7])
            eq = EquipoDTO(idEquipo=r[0], placa=r[1], Elemento=el, Laboratorio=l, Estado=es)
            equipos[r[0]] = eq

        cur.close()
        conn.close()
        return equipos

    def seleccionar(self,placa) -> EquipoDTO:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.seleccionar(placa))
        r = cur.fetchone()

        cur.close()
        conn.close()
        if r is None:
            return None
        
        el = ElementoDTO(idElemento=r[2], descripcion=r[3])
        l = LaboratorioDTO(idLaboratorio=r[4], nombre=r[5])
        es = EstadoDTO(idEstado=r[6], descripcion=r[7])
        return EquipoDTO(idEquipo=r[0], placa=r[1], Elemento=el, Laboratorio=l, Estado=es)
    
    def actualizar_estado(self,idEquipo,idEstado):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.actualizar_estado(idEquipo,idEstado))
        conn.commit()
        cur.close()
        conn.close()

    def insertar(self,placa="",idElemento=None,idLaboratorio=None):
        conn = get_conn()
        cur = conn.cursor()
        try:
            sql, params = DAO.insertar(placa, idElemento, idLaboratorio)
            cur.execute(sql, params)
            conn.commit()
            return "OK", "Equipo registrado correctamente."
        except sqlite3.IntegrityError as e:
            # UNIQUE, FK, NOT NULL 전부 여기로 옴
            if "UNIQUE constraint failed: Equipo.placa" in str(e):
                return "ERROR","La placa ya existe"
            else:
                return str(e)
        finally:
            cur.close()
            conn.close()
    
    def editar(self,idEquipo,placa="",idElemento=None,idLaboratorio=None):
        conn = get_conn()
        cur = conn.cursor()
        
        try:
            sql, params = DAO.editar(idEquipo,placa,idElemento,idLaboratorio)
            cur.execute(sql, params)
            conn.commit()
            return "OK", "Equipo modificado correctamente."
        except sqlite3.IntegrityError as e:
            # UNIQUE, FK, NOT NULL 전부 여기로 옴
            if "UNIQUE constraint failed: Equipo.placa" in str(e):
                return "ERROR","La placa ya existe"
            else:
                return str(e)
        finally:
            cur.close()
            conn.close()
    
    def delete(self,idEquipo):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.delete(idEquipo))
        conn.commit()
        cur.close()
        conn.close()