class EstudianteDAO:
    @staticmethod
    def listar(inf = "", proyecto_c="", multado = False,no_entregado = False):
        # 기본 SELECT (화면에 보여줄 4개 컬럼)
        query = """
            SELECT DISTINCT
                e.idEstudiante, e.nombre, e.apellido, e.correo,
                e.celular, e.codigo, e.cedula,
                pc.idProyecto_C, pc.nombre
            FROM Estudiante e
            LEFT JOIN Proyecto_C pc ON pc.idProyecto_C = e.idProyecto_C
        """

        condiciones = []

        if inf:
            condiciones.append(f"e.cedula = '{inf}' or e.codigo = '{inf}'")

        if proyecto_c:
            condiciones.append(f"pc.nombre = '{proyecto_c}'")

        if multado:
            condiciones.append("p.multa > 0")

        # ------- no_entregado 필터 (hora_final IS NULL) -------
        if no_entregado:
            condiciones.append("p.hora_final IS NULL AND  p.idPrestamo IS NOT NULL")

        if multado or no_entregado:
            query += "JOIN Prestamo p ON e.idEstudiante = p.idEstudiante"
        # ---- WHERE 붙이기 ----
        if condiciones:
            query += " WHERE " + " OR ".join(condiciones)
        return query
    
    @staticmethod
    def seleccionar(inf_estudiante):
        return (
            f"SELECT e.idEstudiante, e.nombre, e.apellido, e.correo, e.celular, e.codigo, e.cedula, "
            f"pc.idProyecto_C, pc.nombre "
            f"FROM Estudiante e "
            f"LEFT JOIN Proyecto_C pc ON (pc.idProyecto_C = e.idProyecto_C) "
            f"WHERE (e.codigo = '{inf_estudiante}' OR e.cedula = '{inf_estudiante}')"
        )

    @staticmethod
    def registrar(nombre, apellido, correo, celular, codigo, cedula, idProyecto_C=None):
        # 1. 쿼리문 작성 (? 파라미터 바인딩 사용)
        query = """
            INSERT INTO Estudiante 
            (nombre, apellido, correo, celular, codigo, cedula, idProyecto_C)
            VALUES (?, ?, ?, ?, ?, ?, ?);
        """
        
        params = [
            nombre, apellido, correo, celular, 
            codigo, cedula, idProyecto_C
        ]

        return query, params
    
    @staticmethod
    def editar(id_estudiante, nombre, apellido, correo, celular, codigo, cedula, idProyecto_C=None):
        # 1. 공통 필드와 파라미터 정의
        fields = [
            "nombre = ?", "apellido = ?", "correo = ?", 
            "celular = ?", "codigo = ?", "cedula = ?",
            "idProyecto_C = ?"  # 항상 포함
        ]
        
        # 2. 파라미터 리스트 생성 (idProyecto_C는 None이면 DB에서 NULL로 처리됨)
        params = [
            nombre, apellido, correo, celular, codigo, cedula, idProyecto_C
        ]

        # 3. 쿼리 조립 (join을 사용해 콤마 문제를 완벽히 해결)
        query = f"UPDATE Estudiante SET {', '.join(fields)} WHERE idEstudiante = ?;"
        
        # 4. WHERE 절을 위한 ID 추가
        params.append(id_estudiante)

        return query, params
    
    @staticmethod
    def delete(idEstudiante):
        return (
            f"DELETE FROM Estudiante "
            f"WHERE idEstudiante = '{idEstudiante}'"
        )
