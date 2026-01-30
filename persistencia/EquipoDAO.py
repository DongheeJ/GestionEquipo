class EquipoDAO:
    @staticmethod
    def seleccionar(placa):
        return (
            f"SELECT e.idEquipo, e.placa, el.idElemento, el.descripcion,"
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
            if placa == 'None':
                condiciones.append(f"eq.placa IS NULL")
            else:
                condiciones.append(f"eq.placa = '{placa}'")

        if laboratorio:
            if laboratorio == 'None':
                condiciones.append(f"eq.idLaboratorio IS NULL")
            else:
                condiciones.append(f"l.nombre = '{laboratorio}'")

        if elemento:
            if elemento == 'None':
                condiciones.append(f"eq.idElemento IS NULL")
            else:
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
        
        if placa is not None and str(placa).strip() != "":
            campos.append("placa")
            placeholders.append("?")
            params.append(str(placa))

        if idElemento is not None:
            campos.append("idElemento")
            placeholders.append("?")
            params.append(int(idElemento))

        if idLaboratorio is not None:
            # print(placa,idElemento,idLaboratorio)
            campos.append("idLaboratorio")
            placeholders.append("?")
            params.append(int(idLaboratorio))

        campos.append("idEstado")
        placeholders.append("?")
        params.append(1)

        sql = f"INSERT OR IGNORE INTO Equipo ({', '.join(campos)}) VALUES ({', '.join(placeholders)})"

        # print(sql,tuple(params))
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
