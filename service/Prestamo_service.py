from persistencia.Conexion import get_conn
from persistencia.Prestamo_DAO import Prestamo_DAO as DAO
from model.PrestamoDTO import PrestamoDTO
from service.Estudiante_service import Estudiante_service
from service.Equipo_service import Equipo_service
from typing import List

class Prestamo_service:
    def __init__(self):
        pass

    def listar(self, estudiante="", equipo="", multados=False, no_entregados=False, entregados=False) -> List[PrestamoDTO]:
        eService = Estudiante_service()
        eqService = Equipo_service()

        conn = get_conn()
        cur = conn.cursor()

        estudiantes = eService.mapear(inf=estudiante)
        equipos = eqService.mapear(placa=equipo)

        cur.execute(DAO.listar(multados,no_entregados,entregados))

        rs = cur.fetchall()

        prestamos = []
        for r in rs:
            e = estudiantes.get(r[4])
            eq = equipos.get(r[5])
            if e is None or eq is None:
                continue
            p = PrestamoDTO(r[0],r[1],r[2],r[3],e,eq)
            prestamos.append(p)

        cur.close()
        conn.close()
        return prestamos
    
    # def mapear(self) -> List[PrestamoDTO]:
    #     eService = Estudiante_service()
    #     eqService = Equipo_service()

    #     conn = get_conn()
    #     cur = conn.cursor()

    #     estudiantes = eService.mapear()
    #     equipos = eqService.mapear()

    #     cur.execute(DAO.listar())
    #     rs = cur.fetchall()

    #     prestamos = {}
    #     for r in rs:
    #         e = estudiantes[r[4]]
    #         eq = equipos[r[5]]
    #         p = PrestamoDTO(r[0],r[1],r[2],r[3],e,eq)
    #         prestamos[r[0]] = p

    #     cur.close()
    #     conn.close()
    #     return prestamos
    
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
    
    def seleccionar_ultimo(self,idEstudiante,idEquipo) -> PrestamoDTO:
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

    def pagar_multa(self,idPrestamo,multa):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.pagar_multa(idPrestamo,multa))
        conn.commit()
        cur.close()
        conn.close()

    def delete(self,idPrestamo):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.delete(idPrestamo))
        conn.commit()
        cur.close()
        conn.close()