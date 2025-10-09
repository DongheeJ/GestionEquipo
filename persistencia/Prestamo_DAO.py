class Prestamo_DAO:
    @staticmethod
    def es_prestamo_entregado(placa, inf_estudiante):
        query = f"""
            SELECT p.hora_final
            FROM Prestamo p
            JOIN Estudiante e ON p.idEstudiante = e.idEstudiante
            JOIN Equipo eq ON p.idEquipo = eq.idEquipo
            WHERE eq.placa = '{placa}'
            AND (e.codigo = '{inf_estudiante}' OR e.cedula = '{inf_estudiante}')
            ORDER BY p.idPrestamo DESC
            LIMIT 1;
        """
        return query
    
    def registrar(hora_inicio,multa,idEstudiante,idEquipo):
        query = f"""
            insert into Prestamo (hora_inicio,multa,idEstudiante,idEquipo) 
            values ('{hora_inicio}',{multa},{idEstudiante},{idEquipo});
        """
        return query