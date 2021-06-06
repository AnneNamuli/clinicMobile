from typing import Optional
from datetime import datetime
from pydantic import BaseModel
from enum import Enum


class Event(str, Enum):
    created='created'
    updated='updated'
    deleted='deleted'


# Shared properties
class LogBase(BaseModel):
    clinic_id: int = None
    patient_id: int = None
    created_at: datetime = None
    event: Event = None


# Properties to receive via API on creation
class LogCreate(LogBase):
    clinic_id: str
    patient_id: str
    event: Event


# Properties to receive via API on update
class LogUpdate(LogBase):
    clinic_id: Optional[int] = None
    patient_id: Optional[int] = None
    event: Optional[Event] = None


class LogInDBBase(LogBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Log(LogInDBBase):
    pass


# Additional properties stored in DB
class LogInDB(LogInDBBase):
    pass