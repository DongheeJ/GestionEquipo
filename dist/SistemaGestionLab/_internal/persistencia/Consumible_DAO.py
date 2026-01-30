class Consumible_DAO:
    @staticmethod
    def listar():
        return "select idConsumible,descripcion,idPrestamo from Consumible"
    @staticmethod
    def registrar(descripcion="",idPrestamo=0):
        query = f"""
            insert into Consumible (descripcion,idPrestamo) 
            values ('{descripcion}',{idPrestamo});
        """
        return query
    @staticmethod
    def listar_por_prestamo(idPrestamo):
        query = f"""
            SELECT c.idConsumible,c.descripcion,c.idPrestamo 
            FROM Consumible c
            WHERE idPrestamo = '{idPrestamo}' 
            """
        return query