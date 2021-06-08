from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Log])
def read_patient_booking_logs(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve all patient booking logs.
    """
    if current_user:
        logs = crud.logs.get_multi(db, skip=skip, limit=limit)
        return logs
    else:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )


@router.get("/{clinic_id}", response_model=List[schemas.Log])
def read_patient_booking_logs_by_clinic_id(
    clinic_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get all patient booking logs for specific clinic by id.
    """

    if current_user:
        logs = crud.logs.get_by_clinic_id(db, clinic_id=clinic_id)
        return logs

    else:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )


@router.post("/", response_model=schemas.Log)
def create_patient_booking_log(
    *,
    db: Session = Depends(deps.get_db),
    log_in: schemas.LogCreate,
    current_user: models.db_tables.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new patient booking log at clinic.
    """
    if current_user:
        logs = crud.logs.create(db=db, obj_in=log_in)
        return logs
    else:
        raise HTTPException(
            status_code=401,
            detail="User does not have enough permissions",
        )


@router.get("/{patient_id}/Bookings/", response_model=List[schemas.Log])
def read_patient_booking_logs_by_patient_id(
    patient_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get all patient booking logs.
    """

    if current_user:
        log = crud.logs.get_by_patient_id(db=db, patient_id=patient_id)
        return log

    else:
        raise HTTPException(
            status_code=401, detail="The user doesn't have enough privileges"
        )

