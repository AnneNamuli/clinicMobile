from typing import Optional
from datetime import datetime

from pydantic import BaseModel, EmailStr


# Shared properties
class ClinicBase(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    contact_number: Optional[str] = None
    last_updated_at: Optional[datetime] = None
    created_at: Optional[datetime] = None


# Properties to receive via API on creation
class ClinicCreate(ClinicBase):
    name: str
    address: str
    contact_number: str


# Properties to receive via API on update
class ClinicUpdate(ClinicBase):
    name: Optional[str] = None
    address: Optional[str] = None
    contact_number: Optional[str] = None
    last_updated_at: Optional[datetime] = None


class ClinicInDBBase(ClinicBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Clinic(ClinicInDBBase):
    pass


# Additional properties stored in DB
class ClinicInDB(ClinicInDBBase):
    pass