# Directorio de Empleados API

API REST desarrollada con FastAPI para la gestión de un directorio corporativo. Permite la administración de empleados y departamentos, incluyendo la funcionalidad de carga de imágenes de perfil y filtrado de datos.

El sistema utiliza SQLModel como ORM y está contenerizado mediante Docker, con una base de datos PostgreSQL.

## Tecnologías Utilizadas

* **Lenguaje:** Python 3.12
* **Framework:** FastAPI
* **ORM:** SQLModel (SQLAlchemy + Pydantic)
* **Base de Datos:** PostgreSQL 15
* **Contenerización:** Docker y Docker Compose
* **Servidor:** Uvicorn

## Estructura del Proyecto

La arquitectura del proyecto sigue un patrón de diseño modular por capas:

```text
DirectorioEmpleadosAPI/
├── app/
│   ├── core/           # Configuración (config.py)
│   ├── db/             # Conexión a Base de Datos (session.py)
│   ├── models/         # Modelos de Base de Datos (SQLModel)
│   ├── routers/        # Definición de rutas (endpoints)
│   ├── schemas/        # Esquemas Pydantic (Request/Response)
│   ├── services/       # Lógica de negocio
│   ├── static/         # Archivos estáticos e imágenes subidas
│   └── main.py         # Punto de entrada de la aplicación
├── .env                # Variables de entorno
├── docker-compose.yml  # Orquestación de servicios
├── Dockerfile          # Construcción de la imagen
└── requirements.txt    # Dependencias
