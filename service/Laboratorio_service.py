from persistencia.Conexion import get_conn
from persistencia.Laboratorio_DAO import Laboratorio_DAO as DAO
from model.LaboratorioDTO import LaboratorioDTO
from typing import List, Dict

class Laboratorio_service:
    def __init__(self):
        pass

    def listar(self, nombre="") -> List[LaboratorioDTO]: 
        conn = get_conn()
        cur = conn.cursor()
        # DAO.listar()의 반환값을 언패킹하여 전달
        query, params = DAO.listar(nombre)
        cur.execute(query, params)
        
        rs = cur.fetchall()
        laboratorios = []
        for r in rs:
            p = LaboratorioDTO(idLaboratorio=r[0], nombre=r[1])
            laboratorios.append(p)

        cur.close()
        conn.close()
        return laboratorios

    def mapear_por_nombre(self) -> Dict[str, LaboratorioDTO]:
        """엑셀 임포트 시 이름으로 ID를 찾기 위한 매핑용 함수"""
        conn = get_conn()
        cur = conn.cursor()
        
        # 전체 리스트 조회
        query, params = DAO.listar()
        cur.execute(query, params)
        
        rs = cur.fetchall()
        mapping = {}
        for r in rs:
            # key: 이름, value: DTO 객체
            mapping[r[1]] = LaboratorioDTO(idLaboratorio=r[0], nombre=r[1])

        cur.close()
        conn.close()
        return mapping

    def insertar(self, nombre):
        conn = get_conn()
        cur = conn.cursor()
        # DAO.insertar 반환값을 언패킹(*)하여 쿼리와 파라미터를 동시에 전달
        cur.execute(*DAO.insertar(nombre))
        conn.commit()
        cur.close()
        conn.close()

    def delete(self, idLaboratorio):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(*DAO.delete(idLaboratorio))
        conn.commit()
        cur.close()
        conn.close()

    def update(self, idLaboratorio, nombre):
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(*DAO.update(idLaboratorio, nombre))
        conn.commit()
        cur.close()
        conn.close()