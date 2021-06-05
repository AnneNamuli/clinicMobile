from typing import TYPE_CHECKING
import datetime

from sqlalchemy import Boolean, Column, Integer, String, DateTime, \
    ForeignKey, Date
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .item import Item  # noqa: F401


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, index=True, nullable=False)
    phone_number = Column(String, unique=True, index=True)
    id_number = Column(String, unique=True, index=True)
    gender = Column(String)
    role = Column(String)
    date_of_birth = Column(Date)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    last_updated_at = Column(DateTime)

    items = relationship("Item", back_populates="owner")


class Clinic(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    contact_number = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    last_updated_at = Column(DateTime)
    owner_id = Column(Integer, ForeignKey("user.id"))


class ClinicBooking(Base):
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("user.id"))
    clinic_id = Column(Integer, ForeignKey("clinic.id"))
    appointment_date = Column(DateTime)


class BookingLog(Base):
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("user.id"))
    clinic_id = Column(Integer, ForeignKey("clinic.id"))
    event = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)


class Item(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("user.id"))
    owner = relationship("User", back_populates="items")
