from tkinter import Tk
from service.Equipo_service import Equipo_service
from controller.Equipo_controller import Equipo_controller
from view.Equipo_view import Equipo_view
from view.Prestamo_view import Prestamo_view

if __name__ == "__main__":
    root = Tk()
    # view = Equipo_view(root)
    # service = Equipo_service()
    # controller = Equipo_controller(service, view)
    view = Prestamo_view(root)
    root.mainloop()