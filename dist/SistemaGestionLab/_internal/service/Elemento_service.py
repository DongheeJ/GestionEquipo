from persistencia.Conexion import get_conn
from persistencia.Elemento_DAO import Elemento_DAO as DAO
from model.ElementoDTO import ElementoDTO
from typing import List,Dict

class Elemento_service:
    def __init__(self):
        pass

    def listar(self,descripcion="") -> List[ElementoDTO]: 
        conn = get_conn()
        cur = conn.cursor()
        query,params = DAO.listar(descripcion.strip())
        cur.execute(query,params)
        rs = cur.fetchall()

        elementos = []
        for r in rs:
            p = ElementoDTO(idElemento=r[0], descripcion=r[1],cantidad=r[2])
            elementos.append(p)

        cur.close()
        conn.close()
        return elementos

    def mapear_por_nombre(self) -> Dict[str, ElementoDTO]:
        conn = get_conn()
        cur = conn.cursor()
        
        # DAO.listar()가 (query, params)를 반환하므로 언패킹(*) 사용
        query, params = DAO.listar()
        cur.execute(query, params)
        
        rs = cur.fetchall()
        elementos = {}
        for r in rs:
            # r[0]: idElemento, r[1]: descripcion
            el = ElementoDTO(idElemento=r[0], descripcion=r[1])
            elementos[r[1]] = el # 이름을 키로 저장하여 매핑 용이하게 함

        cur.close()
        conn.close()
        return elementos

    def insertar(self, descripcion=""):
        conn = get_conn()
        cur = conn.cursor()
        # DAO.insertar 반환값을 언패킹하여 전달
        cur.execute(*DAO.insertar(descripcion.strip()))
        conn.commit()
        cur.close()
        conn.close()

    def delete(self, idElemento):
        conn = get_conn()
        cur = conn.cursor()
        # DAO.delete 반환값을 언패킹하여 전달
        cur.execute(*DAO.delete(idElemento))
        conn.commit()
        cur.close()
        conn.close()

    def update(self, idElemento, descripcion=""):
        conn = get_conn()
        cur = conn.cursor()
        # DAO.update 반환값을 언패킹하여 전달
        cur.execute(*DAO.update(idElemento, descripcion.strip()))
        conn.commit()
        cur.close()
        conn.close()
