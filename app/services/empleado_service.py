import shutil

from sqlmodel import Session, select
from fastapi import Depends, HTTPException, UploadFile
from app.models.empleado import Empleado
from app.models.departamento import Departamento
from app.schemas.empleado import EmpleadoCreate, EmpleadoUpdate
from app.db.session import get_session
import os

class EmpleadoService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, data: EmpleadoCreate) -> Empleado:
        # Validación: ¿Existe el departamento?
        dep = self.session.get(Departamento, data.department_id)
        if not dep:
            raise HTTPException(status_code=400, detail="El departamento especificado no existe")

        db_emp = Empleado.model_validate(data)
        self.session.add(db_emp)
        self.session.commit()
        self.session.refresh(db_emp)
        return db_emp

    def get_all(self):
        # Aquí podrías usar .options(selectinload(Empleado.department)) si necesitas traer el objeto dep
        return self.session.exec(select(Empleado)).all()

    def get_by_id(self, id: int):
        emp = self.session.get(Empleado, id)
        if not emp:
            raise HTTPException(status_code=404, detail="Empleado no encontrado")
        return emp

    def update(self, id: int, data: EmpleadoUpdate) -> Empleado:
        db_emp = self.get_by_id(id)

        # Si se intenta cambiar el departamento, validamos que el nuevo exista
        if data.department_id is not None:
            dep = self.session.get(Departamento, data.department_id)
            if not dep:
                raise HTTPException(status_code=400, detail="El nuevo departamento no existe")

        emp_data = data.model_dump(exclude_unset=True)
        for key, value in emp_data.items():
            setattr(db_emp, key, value)

        self.session.add(db_emp)
        self.session.commit()
        self.session.refresh(db_emp)
        return db_emp

    def delete(self, id: int):
        db_emp = self.get_by_id(id)
        self.session.delete(db_emp)
        self.session.commit()
        return {"message": "Empleado eliminado exitosamente"}

    async def save_image(self, file: UploadFile) -> str:
        upload_dir = "app/static/uploads"

        # Asegura que la carpeta existe
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)

        # Construye la ruta del archivo
        file_path = os.path.join(upload_dir, file.filename)

        # Guarda el contenido del archivo en el servidor
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Devuelve la ruta relativa para guardar en la BD
        return f"/static/uploads/{file.filename}"