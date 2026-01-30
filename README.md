# GestionEquipo
📋 Sistema de Gestión de Equipos de Laboratorio - Guía de Uso
Este software ha sido diseñado para facilitar la administración de inventario, préstamos y devoluciones de equipos de laboratorio.

🚀 Cómo empezar
Para que el programa funcione correctamente, debe descargar la carpeta completa llamada SistemaGestionLab. El programa no funcionará si mueve archivos individuales fuera de esta carpeta.

1. Instrucciones de ejecución
Descomprima el archivo SistemaGestionLab.zip.

Abra la carpeta y busque el archivo llamado SistemaGestionLab.exe.

Haga doble clic en el archivo para iniciar la aplicación.

Consejo: Para mayor comodidad, haga clic derecho en SistemaGestionLab.exe, elija "Enviar a" -> "Escritorio (crear acceso directo)". Así podrá abrirlo desde su escritorio sin mover el archivo original.

2. Notas Importantes (¡Léame!)
Mantener la estructura de carpetas: El archivo .exe depende de las librerías y carpetas internas (como _internal) que lo acompañan. No mueva el archivo ejecutable solo a otra ubicación.

Base de datos: Todos sus datos se guardan en el archivo GestionEquipo.db ubicado en la misma carpeta. Si borra o renombra este archivo, se perderá toda la información.

Copia de seguridad: Se recomienda copiar el archivo GestionEquipo.db periódicamente a una ubicación segura (como una nube o USB) para evitar la pérdida de datos en caso de fallo del equipo.

🛠️ Funciones Principales
Gestión de Estudiantes y Equipos: Registro, edición, eliminación y consulta.

Sistema de Préstamos: Registro de salidas y control de devoluciones con cálculo automático de multas.

Importación de Inventario: Carga masiva de datos a través de archivos Excel.

Control de Consumibles: Registro de elementos adicionales entregados durante el préstamo.

💻 Requisitos del Sistema
Sistema Operativo: Windows 10 o superior (64 bits recomendado).

No requiere la instalación de Python, SQLite ni ningún software adicional. Es una aplicación independiente.