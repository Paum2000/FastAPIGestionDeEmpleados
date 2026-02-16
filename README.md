# FastAPI Gestión de Empleados

[![FastAPI](https://img.shields.io/badge/FastAPI-00584C?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

Una API RESTful robusta y escalable para la gestión de empleados y departamentos, construida con **FastAPI**. Este proyecto permite realizar operaciones CRUD completas con validación de datos automática y documentación interactiva.

---

## Tabla de Contenidos

- [Características](#-características)
- [Requisitos](#-requisitos)
- [Configuración de Variables de Env](#-configuración-de-variables-de-entorno)
- [Instalación y Uso](#-instalación-y-uso)
- [Docker](#-docker)
- [Endpoints de la API](#-endpoints-de-la-api)
- [Documentación](#-documentación)
- [Licencia](#-licencia)

---

## Características

- **Operaciones CRUD:** Gestión completa de Empleados y Departamentos.
- **Validación de Datos:** Uso de Pydantic para asegurar tipos de datos correctos.
- **Documentación Automática:** Swagger UI y ReDoc integrados.
- **Preparado para Producción:** Configuración lista para Docker y variables de entorno.

## Requisitos

Para ejecutar este proyecto localmente, asegúrate de tener:

- **Python 3.9+**
- **pip** (gestor de paquetes de Python)
- **Virtualenv** (recomendado)
- **Docker** (opcional para despliegue en contenedores)

---

## Configuración de Variables de Entorno

El proyecto utiliza variables de entorno para su configuración. Crea un archivo `.env` en la raíz del proyecto basándote en el siguiente esquema:

| Variable | Descripción | Valor Ejemplo |
| :--- | :--- | :--- |
| `DATABASE_URL` | URL de conexión a la base de datos | `sqlite:///./empleados.db` |
| `APP_DEBUG` | Activa el modo de depuración | `True` |
| `API_PORT` | Puerto donde correrá la API | `8081` |
| `SECRET_KEY` | Llave para seguridad/tokens | `tu_llave_secreta_aqui` |

---

## Instalación y Uso

### 1. Clonar el repositorio
```bash
git clone [https://github.com/Paum2000/FastAPIGestionDeEmpleados.git](https://github.com/Paum2000/FastAPIGestionDeEmpleados.git)
cd FastAPIGestionDeEmpleados
```

### 2. Configurar entorno virtual
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/macOS:
source venv/bin/activate
```
### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```
### 4. Ejecutar la aplicación
```bash
uvicorn main:app --host 0.0.0.0 --port 8081 --reload
```
## Docker
Si prefieres ejecutar la aplicación mediante Docker, sigue estos pasos:

- Construir la imagen:
```bash
docker build -t fastapi-gestion-empleados .
```
- Ejecutar el contenedor:
```bash
docker run -d --name empleados-api -p 8081:8081 --env-file .env fastapi-gestion-empleados
```

## Endpoints

A continuación se detallan los endpoints disponibles:

### Empleados
- **GET** `/empleados`: Obtener la lista de todos los empleados.
- **GET** `/empleados/{id}`: Obtener un empleado específico por su ID.
- **POST** `/empleados`: Crear un nuevo empleado.
- **PUT** `/empleados/{id}`: Actualizar un empleado existente.
- **DELETE** `/empleados/{id}`: Eliminar un empleado por su ID.

### Departamento
- **GET** `/departamentos`: Obtener la lista de todos los departamentos.
- **GET** `/departamentos/{id}`: Obtener un departamento específico por su ID.
- **POST** `/departamentos`: Crear un nuevo departamento.
- **PUT** `/departamentos/{id}`: Actualizar un departamento existente.
- **DELETE** `/departamentos/{id}`: Eliminar un departamento por su ID.

## Documentación

Una vez que la aplicación esté en funcionamiento, puedes explorar y probar los endpoints de la API de forma interactiva a través de los siguientes enlaces:

* **Swagger UI (Recomendado):** [http://localhost:8081/docs](http://localhost:8081/docs)
* **ReDoc:** [http://localhost:8081/redoc](http://localhost:8081/redoc)

## Licencia

Este proyecto está bajo la licencia **MIT**.

---

## Desarrollado por

**Paum2000** _¡Gracias por visitar este repositorio!_


