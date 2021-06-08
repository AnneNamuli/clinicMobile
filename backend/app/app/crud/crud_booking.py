from typing import Any, Dict, Optional, Union

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.db_tables import ClinicBooking, User, Clinic
from app.schemas.booking import BookingCreate, BookingUpdate


class CRUDUser(CRUDBase[ClinicBooking, BookingCreate, BookingUpdate]):
    def get_by_id(self, db: Session, *, id: int) -> Optional[ClinicBooking]:
        return db.query(ClinicBooking).filter(ClinicBooking.id == id).first()

    def get_bookings(self, db: Session):
        return db.query(ClinicBooking.id, User.full_name, User.phone_number, User.date_of_birth, Clinic.name, Clinic.address,
                        ClinicBooking.appointment_date).filter(User.id == ClinicBooking.patient_id).filter(Clinic.id == ClinicBooking.clinic_id).all()

    def get_by_clinic_id(self, db: Session, *, clinic_id: int) -> Optional[ClinicBooking]:
        return db.query(ClinicBooking).filter(ClinicBooking.clinic_id == clinic_id).all()

    def get_by_patient_id(self, db: Session, *, patient_id: int) -> Optional[ClinicBooking]:
        return db.query(ClinicBooking).filter(ClinicBooking.patient_id == patient_id).all()

    def create(self, db: Session, *, obj_in: BookingCreate) -> ClinicBooking:
        db_obj = ClinicBooking(
            clinic_id=obj_in.clinic_id,
            patient_id=obj_in.patient_id,
            appointment_date=obj_in.appointment_date
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: ClinicBooking, obj_in: Union[BookingUpdate, Dict[str, Any]]
    ) -> ClinicBooking:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)


booking = CRUDUser(ClinicBooking)
