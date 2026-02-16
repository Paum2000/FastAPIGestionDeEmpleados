from fastapi import APIRouter, Depends, Query, UploadFile, File
from app.services.empleado_service import EmpleadoService
from app.schemas.empleado import EmpleadoCreate, EmpleadoResponse, EmpleadoUpdate

router = APIRouter(prefix="/empleados", tags=["Empleados"])

@router.post("/", response_model=EmpleadoResponse)
async def create_empleado(
        data: EmpleadoCreate,
        service: EmpleadoService = Depends()
):
    return service.create(data)

@router.get("/", response_model=list[EmpleadoResponse])
async def read_empleados(
        service: EmpleadoService = Depends(),
        department_id: int | None = Query(None, description="Filtrar por ID de departamento"),
        name: str | None = Query(None, description="Buscar por nombre")
):
    # Nota: Tendrías que ajustar el service.get_all() para aceptar estos filtros
    return service.get_all()

@router.get("/{id}", response_model=EmpleadoResponse)
async def read_empleado(id: int, service: EmpleadoService = Depends()):
    return service.get_by_id(id)

@router.patch("/{id}", response_model=EmpleadoResponse)
async def update_empleado(
        id: int,
        data: EmpleadoUpdate,
        service: EmpleadoService = Depends()
):
    return service.update(id, data)

@router.delete("/{id}")
async def delete_empleado(id: int, service: EmpleadoService = Depends()):
    return service.delete(id)

@router.patch("/{id}/image", response_model=EmpleadoResponse)
async def upload_empleado_image(
        id: int,
        file: UploadFile = File(...),
        service: EmpleadoService = Depends()
):
    # 1. Guardamos la imagen y obtenemos el string
    image_url = await service.save_image(file)

    # 2. USAR EL NOMBRE CORRECTO: image_uri
    # Si usas 'imagen', Pydantic lo ignora y manda un objeto vacío
    empleado_update = EmpleadoUpdate(image_uri=image_url)

    # 3. Actualizamos
    return service.update(id, empleado_update)