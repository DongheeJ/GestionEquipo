from service.Estudiante_service import Estudiante_service
from service.Proyecto_C_service import Proyecto_C_service
from service.Equipo_service import Equipo_service
from service.Estado_service import Estado_service
from service.Laboratorio_service import Laboratorio_service
from service.Elemento_service import Elemento_service



if __name__ == "__main__":
    estudiante_service= Estudiante_service()
    estudiantes = estudiante_service.listar()
    print("estudiantes____________________________")
    for e in estudiantes:
        print(e.nombre,e.celular,e.proyecto_c.nombre)
    
    proyecto_C_service = Proyecto_C_service()
    proyectos_C = proyecto_C_service.listar()
    print("proyecto_C_________________________s_____")
    for pc in proyectos_C:
        print(pc.nombre)

    
    # === Equipos ===
    equipo_service = Equipo_service()
    equipos = equipo_service.listar()
    print("\nEQUIPOS ________________________________")
    for eq in equipos:
        print(
            f"ID: {eq.get_idEquipo()} | Placa: {eq.get_placa()} | "
            f"Elemento: {eq.get_Elemento().get_descripcion()} "
            f"({eq.get_Elemento().get_cantidad()}) | "
            f"Laboratorio: {eq.get_Laboratorio().get_descripcion()} | "
            f"Estado: {eq.get_Estado().get_descripcion()}"
        )

    # === Elementos ===
    elemento_service = Elemento_service()
    elementos = elemento_service.listar()
    print("\nELEMENTOS ______________________________")
    for el in elementos:
        print(f"{el.get_idElemento()} | {el.get_descripcion()} | Cantidad: {el.get_cantidad()}")

    # === Laboratorios ===
    laboratorio_service = Laboratorio_service()
    laboratorios = laboratorio_service.listar()
    print("\nLABORATORIOS ___________________________")
    for lab in laboratorios:
        print(f"{lab.get_idLaboratorio()} | {lab.get_descripcion()}")

    # === Estados ===
    estado_service = Estado_service()
    estados = estado_service.listar()
    print("\nESTADOS ________________________________")
    for es in estados:
        print(f"{es.get_idEstado()} | {es.get_descripcion()}")

        
