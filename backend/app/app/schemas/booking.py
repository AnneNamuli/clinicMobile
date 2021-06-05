from typing import Optional
from datetime import datetime

from pydantic import BaseModel


# Shared properties
class BookingBase(BaseModel):
    clinic_id: int = None
    patient_id: int = None
    appointment_date: datetime = None


# Properties to receive via API on creation
class BookingCreate(BookingBase):
    clinic_id: str
    patient_id: str
    appointment_date: datetime


# Properties to receive via API on update
class BookingUpdate(BookingBase):
    clinic_id: Optional[int] = None
    patient_id: Optional[int] = None
    appointment_date: Optional[datetime] = None


class BookingInDBBase(BookingBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Booking(BookingInDBBase):
    pass


# Additional properties stored in DB
class BookingInDB(BookingInDBBase):
    pass