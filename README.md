# FastAPI Gestión de Empleados

Una API RESTful para la gestión de empleados, construida con FastAPI. Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los registros de empleados.

## Tabla de Contenidos

- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Endpoints](#endpoints)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Características

- Gestión de empleados con operaciones CRUD.
- Validación de datos utilizando Pydantic.
- Documentación automática de la API con Swagger UI y ReDoc.
- Soporte para autenticación y autorización (si está implementado).

## Requisitos

Para ejecutar este proyecto, necesitarás tener instalados los siguientes componentes:

- Python 3.7 o superior
- FastAPI
- Uvicorn
- (Otras dependencias que puedas tener)

Puedes instalar las dependencias necesarias utilizando `pip`:

```bash
pip install fastapi uvicornInstalaciónClona el repositorio:
git clone https://github.com/Paum2000/FastAPIGestionDeEmpleados.git
```

Navega al directorio del proyecto:
```bash
cd FastAPIGestionDeEmpleados
```

Instala las dependencias:
```bash
pip install -r requirements.txt
```

##Uso

Para iniciar la aplicación, ejecuta el siguiente comando: 
app --reload
La aplicación se ejecutará en http://127.0.0.1:8081.

##Endpoints

A continuación se detallan los endpoints disponibles:
- Empleados
GET /empleados: Obtener la lista de todos los empleados.
GET /empleados/{id}: Obtener un empleado específico por su ID.
POST /empleados: Crear un nuevo empleado.
PUT /empleados/{id}: Actualizar un empleado existente.
DELETE /empleados/{id}: Eliminar un empleado por su ID.

- Departamento
GET /departamentos: Obtener la lista de todos los departamentos.
GET /departamentos/{id}: Obtener un departamento específico por su ID.
POST /departamentos: Crear un nuevo departamento.
PUT /departamentos/{id}: Actualizar un departamento existente.
DELETE /departamentos/{id}: Eliminar un departamento por su ID.

La documentación de la API está disponible en http://127.0.0.1:8081/docs.

