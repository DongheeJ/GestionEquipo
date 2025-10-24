import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from service.Equipo_service import Equipo_service
from datetime import datetime
if __name__ == "__main__":
    service = Equipo_service()
    print(service.seleccionar("ABC123").get_placa())