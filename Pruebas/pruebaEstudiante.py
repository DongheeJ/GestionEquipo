import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from service.Estudiante_service import Estudiante_service
from datetime import datetime
if __name__ == "__main__":
    estudiante_service = Estudiante_service()
    print(estudiante_service.seleccionar("20222578117").get_proyecto_c().get_nombre())