from persistencia.Conexion import get_conn
from persistencia.Laboratorio_DAO import Laboratorio_DAO as DAO
from model.LaboratorioDTO import LaboratorioDTO

class Laboratorio_service:
    def __init__(self):
        pass

    def listar(self): 
        conn = get_conn()
        cur = conn.cursor()
        cur.execute(DAO.listar())
        rs = cur.fetchall()

        laboratorios = []
        for r in rs:
            p = LaboratorioDTO(idLaboratorio=r[0], descripcion=r[1])
            laboratorios.append(p)

        conn.close()
        return laboratorios