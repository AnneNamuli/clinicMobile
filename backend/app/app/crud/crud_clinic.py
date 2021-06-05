from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.crud.base import CRUDBase
from app.models.db_tables import Clinic
from app.schemas.clinic import ClinicCreate, ClinicUpdate


class CRUDUser(CRUDBase[Clinic, ClinicCreate, ClinicUpdate]):
    def get_by_id(self, db: Session, *, id: int) -> Optional[Clinic]:
        return db.query(Clinic).filter(Clinic.id == id).first()

    def get_by_id(self, db: Session, *, id: int) -> Optional[Clinic]:
        return db.query(Clinic).filter(Clinic.id == id).first()

    def search(self, db: Session, *, param: str) -> Optional[Clinic]:
        return db.query(Clinic).filter(or_(Clinic.address.ilike(param), Clinic.name.ilike(param))).all()

    def create(self, db: Session, *, obj_in: ClinicCreate) -> Clinic:
        db_obj = Clinic(
            name=obj_in.name,
            address=obj_in.address,
            contact_number=obj_in.contact_number
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Clinic, obj_in: Union[ClinicUpdate, Dict[str, Any]]
    ) -> Clinic:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)


clinic = CRUDUser(Clinic)
