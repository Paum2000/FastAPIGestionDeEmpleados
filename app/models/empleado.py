from sqlmodel import SQLModel,Field, Relationship
from typing import Optional

class Empleado(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(nullable=False)
    description: Optional[str] = None
    image_uri: Optional[str] = None

    # Clave foránea
    department_id: int = Field(foreign_key="departamento.id")

    # Relación de objeto
    department: Optional["Departamento"] = Relationship(back_populates="empleados")