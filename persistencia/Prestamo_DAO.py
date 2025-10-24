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
    
    def registrar(hora_inicio,multa,idEstudiante,idEquipo):
        query = f"""
            insert into Prestamo (hora_inicio,multa,idEstudiante,idEquipo) 
            values ('{hora_inicio}',{multa},{idEstudiante},{idEquipo});
        """
        return query
    
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
    
    def entregar(hora_final,multa,idPrestamo):
        query = f"""
            UPDATE Prestamo SET hora_final = '{hora_final}',multa = '{multa}'
            where idPrestamo = '{idPrestamo}';
        """
        return query
