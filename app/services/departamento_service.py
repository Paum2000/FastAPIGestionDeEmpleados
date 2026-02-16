from sqlmodel import Session, select
from fastapi import Depends, HTTPException
from app.models.departamento import Departamento
from app.schemas.departamento import DepartamentoCreate, DepartamentoResponse, DepartamentoUpdate
from app.db.session import get_session

class DepartamentoService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create(self, data: DepartamentoCreate) -> Departamento:
        db_dep = Departamento.model_validate(data)
        self.session.add(db_dep)
        self.session.commit()
        self.session.refresh(db_dep)
        return db_dep

    def get_all(self):
        return self.session.exec(select(Departamento)).all()

    def get_by_id(self, id: int):
        dep = self.session.get(Departamento, id)
        if not dep:
            raise HTTPException(status_code=404, detail="Departamento no encontrado")
        return dep

    def update(self, id: int, data: DepartamentoUpdate) -> Departamento:
        db_dep = self.get_by_id(id)
        dep_data = data.model_dump(exclude_unset=True)
        for key, value in dep_data.items():
            setattr(db_dep, key, value)

        self.session.add(db_dep)
        self.session.commit()
        self.session.refresh(db_dep)
        return db_dep

    def delete(self, id: int):
        db_dep = self.get_by_id(id)
        self.session.delete(db_dep)
        self.session.commit()
        return {"message": "Departamento eliminado"}