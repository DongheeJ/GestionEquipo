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
        # f-string 대신 ?를 사용하고, 데이터는 따로 튜플로 반환합니다.
        query = "INSERT OR IGNORE INTO Elemento (descripcion) VALUES (?)"
        return query, (descripcion,)

    @staticmethod
    def delete(id_elemento):
        # id 같은 숫자형태도 ?를 사용하는 것이 안전합니다.
        query = "DELETE FROM Elemento WHERE idElemento = ?"
        return query, (id_elemento,)

    @staticmethod
    def update(id_elemento, descripcion):
        # 콤마(,) 등 문법 오류 수정 및 바인딩 적용
        query = "UPDATE Elemento SET descripcion = ? WHERE idElemento = ?"
        return query, (descripcion, id_elemento)