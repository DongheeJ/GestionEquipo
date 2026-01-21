class Prestamo_DAO:
    @staticmethod
    def es_prestamo_libre(idEquipo):
        query = f"""
            SELECT hora_final
            FROM Prestamo 
            WHERE idEquipo = '{idEquipo}'
            ORDER BY idPrestamo DESC
            LIMIT 1;
        """
        return query
    
    @staticmethod
    def registrar(hora_inicio,multa,idEstudiante,idEquipo):
        query = f"""
            insert into Prestamo (hora_inicio,multa,idEstudiante,idEquipo) 
            values ('{hora_inicio}',{multa},{idEstudiante},{idEquipo});
        """
        return query
    
    @staticmethod
    def seleccionar_ultimo(idEstudiante,idEquipo):
        query = f"""
            SELECT idPrestamo, hora_inicio, hora_final, multa, idEstudiante, idEquipo
            from Prestamo p

            where idEstudiante = '{idEstudiante}'
            and idEquipo = '{idEquipo}'
            and hora_final IS NULL
            ORDER BY p.idPrestamo DESC
            LIMIT 1;
        """
        return query
    
    @staticmethod
    def listar(multados=False, no_entregados=False, entregados=False):

        query = """
            SELECT p.idPrestamo, p.hora_inicio, p.hora_final, p.multa, 
                p.idEstudiante, p.idEquipo
            FROM Prestamo p
        """

        joins = []
        condiciones = []

        if no_entregados:
            condiciones.append("p.hora_final IS NULL")
        if entregados:
            condiciones.append("p.hora_final IS NOT NULL")
        if multados:
            condiciones.append("p.multa > 0")

        if joins:
            query += " " + " ".join(joins)

        if condiciones:
            query += " WHERE " + " OR ".join(condiciones)

        return query
    
    @staticmethod
    def entregar(hora_final,multa,idPrestamo):
        query = f"""
            UPDATE Prestamo SET hora_final = '{hora_final}',multa = '{multa}'
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