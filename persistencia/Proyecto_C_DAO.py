class Proyecto_C_DAO:
    @staticmethod
    def listar(nombre=""):
        if nombre:
            return (
                f"SELECT idProyecto_C, nombre "
                f"FROM Proyecto_C "
                f"WHERE nombre LIKE '%{nombre}%'"
            )
        return "SELECT idProyecto_C, nombre FROM Proyecto_C"

    @staticmethod
    def insertar(nombre):
        return (
            f"INSERT OR IGNORE INTO Proyecto_C (nombre) VALUES ('{nombre}')"
        )

    @staticmethod
    def delete(id_proyecto):

        return (
            f"DELETE FROM Proyecto_C "
            f"WHERE idProyecto_C = '{id_proyecto}'"
        )

    @staticmethod
    def update(id_proyecto, nombre):
        return (
            f"UPDATE Proyecto_C "
            f"SET nombre = '{nombre}' "
            f"WHERE idProyecto_C = {id_proyecto}"
        )