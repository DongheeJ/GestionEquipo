class Prestamo_DAO:
    @staticmethod
    def es_prestamo_libre(idEquipo):
        query = f"""
            SELECT fecha_final
            FROM Prestamo 
            WHERE idEquipo = '{idEquipo}'
            ORDER BY idPrestamo DESC
            LIMIT 1;
        """
        return query
    
    @staticmethod
    def registrar(fecha_inicio,multa,idEstudiante,idEquipo):
        query = f"""
            insert into Prestamo (fecha_inicio,multa,idEstudiante,idEquipo) 
            values ('{fecha_inicio}',{multa},{idEstudiante},{idEquipo});
        """
        return query
    
    @staticmethod
    def seleccionar_ultimo(idEstudiante,idEquipo):
        query = f"""
            SELECT idPrestamo, fecha_inicio, fecha_final, multa, idEstudiante, idEquipo
            from Prestamo p

            where idEstudiante = '{idEstudiante}'
            and idEquipo = '{idEquipo}'
            and fecha_final IS NULL
            ORDER BY p.idPrestamo DESC
            LIMIT 1;
        """
        return query
    
    @staticmethod
    def listar(multados=False, no_entregados=False, entregados=False,
                sort_fecha="",sort_order=""):

        query = """
            SELECT p.idPrestamo, p.fecha_inicio, p.fecha_final, p.multa, 
                p.idEstudiante, p.idEquipo
            FROM Prestamo p
        """

        joins = []
        condiciones = []

        if no_entregados:
            condiciones.append("p.fecha_final IS NULL")
        if entregados:
            condiciones.append("p.fecha_final IS NOT NULL")
        if multados:
            condiciones.append("p.multa > 0")

        if joins:
            query += " " + " ".join(joins)

        if condiciones:
            query += " WHERE " + " OR ".join(condiciones)

        if sort_fecha != "":
            query += " ORDER BY " + sort_fecha+ " "+ sort_order

        return query
    
    @staticmethod
    def entregar(fecha_final,multa,idPrestamo):
        query = f"""
            UPDATE Prestamo SET fecha_final = '{fecha_final}',multa = '{multa}'
            where idPrestamo = '{idPrestamo}';
        """
        return query

    @staticmethod
    def pagar_multa(idPrestamo, monto):
        query = f"""
            UPDATE Prestamo
            SET multa = CASE
                WHEN multa - {monto} < 0 THEN 0
                ELSE multa - {monto}
            END
            WHERE idPrestamo = {idPrestamo};
        """
        return query

    @staticmethod
    def delete(idPrestamo):
        return (
            f"DELETE FROM Prestamo "
            f"WHERE idPrestamo = '{idPrestamo}'"
        )