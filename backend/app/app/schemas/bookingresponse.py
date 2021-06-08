from datetime import datetime, date

from pydantic import BaseModel


# Shared properties
class BookingRepBase(BaseModel):
    id: int = None
    full_name: str = None
    phone_number: str = None
    date_of_birth: date = None
    name: str = None
    address: str = None
    appointment_date: datetime = None

    class Config:
        orm_mode = True


# Properties to receive via API on creation
class BookingRepCreate(BookingRepBase):
    pass


# Properties to receive via API on update
class BookingRepUpdate(BookingRepBase):
    pass


class BookingRepInDBBase(BookingRepBase):
    pass


# Additional properties to return via API
class BookingRep(BookingRepInDBBase):
    pass


# Additional properties stored in DB
class BookingRepInDB(BookingRepInDBBase):
    pass