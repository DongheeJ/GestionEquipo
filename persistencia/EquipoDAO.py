class EquipoDAO:
    @staticmethod
    def seleccionar(placa):
        return (
            f"SELECT e.idEquipo, e.placa, el.idElemento, el.descripcion "
            f"l.idLaboratorio, l.nombre, es.idEstado, es.descripcion "
            f"FROM Equipo e "
            f"LEFT JOIN Elemento el ON (e.idElemento = el.idElemento) "
            f"LEFT JOIN Laboratorio l ON (e.idLaboratorio = l.idLaboratorio) "
            f"JOIN Estado es ON (e.idEstado = es.idEstado) "
            f"WHERE e.placa = '{placa}'"
        )
    @staticmethod
    def actualizar_estado(idEquipo,idEstado):
        query = f"""
            UPDATE Equipo SET idEstado = '{idEstado}'
            where idEquipo = '{idEquipo}';
        """
        return query
    
    @staticmethod
    def listar(placa="", estado="", laboratorio="", elemento=""):
        # 기본 SELECT (화면에 보여줄 4개 컬럼)
        query = """
        SELECT
            eq.idEquipo, eq.placa,
            
            el.idElemento, el.descripcion,
            
            l.idLaboratorio, l.nombre,
            
            es.idEstado, es.descripcion
        FROM Equipo eq
        LEFT JOIN Elemento el ON el.idElemento = eq.idElemento
        LEFT JOIN Laboratorio l ON l.idLaboratorio = eq.idLaboratorio
        JOIN Estado es ON es.idEstado = eq.idEstado
        """

        condiciones = []

        if placa:
            condiciones.append(f"eq.placa = '{placa}'")

        if laboratorio:
            condiciones.append(f"l.nombre = '{laboratorio}'")

        if elemento:
            condiciones.append(f"el.descripcion = '{elemento}'")

        if estado:
            condiciones.append(f"es.descripcion = '{estado}'")

        if condiciones:
            query += " WHERE " + " AND ".join(condiciones)

        return query

    @staticmethod
    def insertar(placa="", idElemento=None, idLaboratorio=None):
        campos = []
        placeholders = []
        params = []

        if placa != "":
            campos.append("placa")
            placeholders.append("?")
            params.append(placa)

        if idElemento is not None:
            campos.append("idElemento")
            placeholders.append("?")
            params.append(idElemento)

        if idLaboratorio is not None:
            campos.append("idLaboratorio")
            placeholders.append("?")
            params.append(idLaboratorio)

        campos.append("idEstado")
        placeholders.append("?")
        params.append(1)

        sql = f"INSERT INTO Equipo ({', '.join(campos)}) VALUES ({', '.join(placeholders)})"
        return sql, tuple(params)
    
    @staticmethod
    def editar(idEquipo, placa="", idElemento=None, idLaboratorio=None):

        campos = []
        params = []

        campos.append("placa = ?")
        params.append(placa if placa != "" else None)

        campos.append("idElemento = ?")
        params.append(idElemento)

        campos.append("idLaboratorio = ?")
        params.append(idLaboratorio)

        sql = f"""
            UPDATE Equipo
            SET {', '.join(campos)}
            WHERE idEquipo = ?
        """
        params.append(idEquipo)

        return sql, tuple(params)

    @staticmethod
    def delete(idEquipo):
        return (
            f"DELETE FROM Equipo "
            f"WHERE idEquipo = '{idEquipo}'"
        )
