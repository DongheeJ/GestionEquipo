class Laboratorio_DAO:
    @staticmethod
    def listar(nombre=""):
        query = "SELECT idLaboratorio, nombre FROM Laboratorio"
        params = []
        
        if nombre:
            query += " WHERE nombre LIKE ?"
            params.append(f"%{nombre}%")
            
        return query, tuple(params)

    @staticmethod
    def insertar(nombre):
        # INSERT OR IGNORE와 파라미터 바인딩 적용
        query = "INSERT OR IGNORE INTO Laboratorio (nombre) VALUES (?)"
        return query, (nombre,)

    @staticmethod
    def delete(idLaboratorio):
        query = "DELETE FROM Laboratorio WHERE idLaboratorio = ?"
        return query, (idLaboratorio,)

    @staticmethod
    def update(idLaboratorio, nombre):
        query = "UPDATE Laboratorio SET nombre = ? WHERE idLaboratorio = ?"
        return query, (nombre, idLaboratorio)