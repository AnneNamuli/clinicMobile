from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.db_tables import BookingLog
from app.schemas.bookinglog import LogCreate, LogUpdate


class CRUDUser(CRUDBase[BookingLog, LogCreate, LogUpdate]):
    def get_by_id(self, db: Session, *, id: int) -> Optional[BookingLog]:
        return db.query(BookingLog).filter(BookingLog.id == id).first()

    def get_by_clinic_id(self, db: Session, *, clinic_id: int) -> Optional[BookingLog]:
        return db.query(BookingLog).filter(BookingLog.clinic_id == clinic_id).all()

    def get_by_patient_id(self, db: Session, *, patient_id: int) -> Optional[BookingLog]:
        return db.query(BookingLog).filter(BookingLog.patient_id == patient_id).all()

    def create(self, db: Session, *, obj_in: LogCreate) -> BookingLog:
        db_obj = BookingLog(
            clinic_id=obj_in.clinic_id,
            patient_id=obj_in.patient_id,
            appointment_date=obj_in.appointment_date
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: BookingLog, obj_in: Union[LogUpdate, Dict[str, Any]]
    ) -> BookingLog:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)


logs = CRUDUser(BookingLog)
