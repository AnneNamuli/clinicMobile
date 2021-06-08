from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Booking])
def read_patient_bookings(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve all patient booking data.
    """
    if current_user:
        booking = crud.booking.get_multi(db, skip=skip, limit=limit)
        return booking
    else:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )


@router.get("/Bookings/{clinic_id}", response_model=List[schemas.Booking])
def read_patient_bookings_by_clinic_id(
    clinic_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get all patient bookings for specific clinic by id.
    """

    if current_user:
        booking = crud.booking.get_by_clinic_id(db, clinic_id=clinic_id)
        return booking

    else:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )


@router.get("/Bookings", response_model=List[schemas.BookingRepBase])
def read_patient_booking_description(
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get all patient bookings.
    """

    if current_user:
        booking = crud.booking.get_bookings(db)
        return booking

    else:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )


@router.get("/{id}", response_model=schemas.Booking)
def read_patient_bookings_by_pk(
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get all patient bookings by id
    """

    if current_user:
        booking = crud.booking.get_by_id(db, id=id)
        return booking
    else:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )


@router.post("/", response_model=schemas.Booking)
def create_patient_booking(
    *,
    db: Session = Depends(deps.get_db),
    booking_in: schemas.BookingCreate,
    current_user: models.db_tables.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new patient booking at clinic.
    """
    if current_user:
        booking = crud.booking.create(db=db, obj_in=booking_in)
        return booking
    else:
        raise HTTPException(
            status_code=401,
            detail="User does not have enough permissions",
        )


@router.get("/{patient_id}/Bookings/", response_model=List[schemas.Booking])
def read_patient_bookings_by_patient_id(
    patient_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get all patient bookings.
    """

    if current_user:
        booking = crud.booking.get_by_patient_id(db=db, patient_id=patient_id)
        return booking

    else:
        raise HTTPException(
            status_code=401, detail="The user doesn't have enough privileges"
        )


@router.patch("/id", response_model=schemas.Booking)
def update_patient_booking(
    id: int,
    *,
    db: Session = Depends(deps.get_db),
    booking_in: schemas.BookingUpdate,
    current_user: models.db_tables.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update patient booking data.
    """
    if current_user:
        booking = crud.booking.get(db, id=id)
        if not booking:
            raise HTTPException(
                status_code=404,
                detail="The clinic booking with this ID does not exist in the system",
            )
        booking = crud.booking.update(db=db, db_obj=booking, obj_in=booking_in)
        return booking
    else:
        raise HTTPException(
            status_code=401,
            detail="User does not have enough permissions",
        )


@router.delete("/{id}", response_model=schemas.Booking)
def delete_patient_booking(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Delete patient booking.
    """
    booking = crud.booking.get(db=db, id=id)
    if not booking:
        raise HTTPException(status_code=404, detail="Patient booking not found")
    if not crud.user.is_superuser(current_user):
        raise HTTPException(status_code=400, detail="User does not have enough permissions")
    booking = crud.booking.remove(db=db, id=id)
    return booking





