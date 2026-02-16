from sqlmodel import SQLModel

class EmpleadoCreate(SQLModel):
    name: str
    description: str | None
    image_uri: str | None
    department_id: int

class EmpleadoResponse(EmpleadoCreate):
    id: int

class EmpleadoUpdate(SQLModel):
    name: str| None = None
    description: str| None = None
    image_uri: str| None = None
    department_id: int | None = None