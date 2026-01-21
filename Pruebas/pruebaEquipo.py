from tkinter import Tk
from service.Equipo_service import Equipo_service
from view.Equipo_view import Equipo_view
from controller.Equipo_controller import Equipo_controller

if __name__ == "__main__":
    
    root = Tk()
    service = Equipo_service()
    view = Equipo_view(root)
    controller = Equipo_controller(service, view)
    root.mainloop()