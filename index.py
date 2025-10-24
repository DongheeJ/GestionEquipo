from tkinter import Tk
from view.Prestamo_view import Prestamo_view
from controller.Prestamo_controller import Prestamo_controller
from service.Prestamo_service import Prestamo_service
from service.Estudiante_service import Estudiante_service
from service.Equipo_service import Equipo_service
from service.Consumible_service import Consumible_service
if __name__ == "__main__":
    root = Tk()

    view = Prestamo_view(root)
    prestamo_service = Prestamo_service()
    estudiante_service = Estudiante_service()
    equipo_service = Equipo_service()
    consumible_service = Consumible_service()

    controller = Prestamo_controller(
        prestamo_service, view,
        estudiante_service=estudiante_service,
        equipo_service=equipo_service,
        consumible_service=consumible_service
    )
    root.mainloop()