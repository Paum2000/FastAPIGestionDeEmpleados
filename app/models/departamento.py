from sqlmodel import SQLModel,Field, Relationship
from typing import List

class Departamento(SQLModel, table=True):
    # El ID es primary_key. En la BD no es opcional,
    # pero en Python se pone Optional para que el motor lo autogenere al crear el objeto.
    id: int | None = Field(default=None, primary_key=True)
    nombre: str = Field(nullable=False) # Campo obligatorio

    empleados: List["Empleado"] = Relationship(back_populates="department")