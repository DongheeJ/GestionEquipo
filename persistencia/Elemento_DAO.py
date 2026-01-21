class Elemento_DAO:
    @staticmethod
    def listar(descripcion=""):
        # 기본 쿼리: Elemento 정보와 해당 Elemento에 속한 Equipo의 개수를 계산
        query = """
            SELECT 
                e.idElemento, 
                e.descripcion, 
                COUNT(eq.idEquipo) AS cantidad
            FROM Elemento e
            LEFT JOIN Equipo eq ON e.idElemento = eq.idElemento
        """
        
        params = []
        
        # 검색어가 있을 경우 WHERE 절 추가
        if descripcion:
            query += " WHERE e.descripcion LIKE ?"
            params.append(f"%{descripcion}%")
        
        # 그룹화 (idElemento별로 묶어서 개수를 셈)
        query += " GROUP BY e.idElemento"
        
        return query, params

    @staticmethod
    def insertar(descripcion):
        return (
            f"INSERT INTO Elemento (descripcion) VALUES ('{descripcion}')"
        )

    @staticmethod
    def delete(id_elemento):
        return (
            f"DELETE FROM Elemento "
            f"WHERE idElemento = '{id_elemento}'"
        )

    @staticmethod
    def update(id_elemento, descripcion, ):
        return (
            f"UPDATE Elemento "
            f"SET descripcion = '{descripcion}' "
            f"WHERE idElemento = {id_elemento}"
        )