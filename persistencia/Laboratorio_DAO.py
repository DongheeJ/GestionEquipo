class Laboratorio_DAO:
    @staticmethod
    def listar(nombre=""):
        if nombre:
            return (
                f"SELECT idLaboratorio, nombre "
                f"FROM Laboratorio "
                f"WHERE nombre LIKE '%{nombre}%'"
            )
        return "SELECT idLaboratorio, nombre FROM Laboratorio"


    @staticmethod
    def insertar(nombre):
        return (
            f"INSERT INTO Laboratorio (nombre) VALUES ('{nombre}')"
        )

    @staticmethod
    def delete(idLaboratorio):

        return (
            f"DELETE FROM Laboratorio "
            f"WHERE idLaboratorio = '{idLaboratorio}'"
        )

    @staticmethod
    def update(idLaboratorio, nombre):
        return (
            f"UPDATE Laboratorio "
            f"SET nombre = '{nombre}' "
            f"WHERE idLaboratorio = {idLaboratorio}"
        )