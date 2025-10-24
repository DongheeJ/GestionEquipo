import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from service.Prestamo_service import Prestamo_service
from datetime import datetime
if __name__ == "__main__":
    prestamo_service = Prestamo_service()
    print(prestamo_service.es_prestamo_entregado("ABC123","20222578117"))
    print(datetime.now().strftime("%Y-%m-%d %H:%M"))