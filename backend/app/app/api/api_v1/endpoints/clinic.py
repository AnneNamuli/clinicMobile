from typing import Any, List

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Clinic])
def read_clinics(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve all clinic data.
    """
    if current_user:
        clinics = crud.clinic.get_multi(db, skip=skip, limit=limit)
        return clinics
    else:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )


@router.get("/{clinic_id}", response_model=schemas.Clinic)
def read_clinic_by_id(
    clinic_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific clinic by id.
    """

    if current_user:
        clinic = crud.clinic.get(db, id=clinic_id)
        return clinic

    else:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )


@router.post("/", response_model=schemas.Clinic)
def create_clinic(
    *,
    db: Session = Depends(deps.get_db),
    clinic_in: schemas.ClinicCreate,
    current_user: models.db_tables.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create new clinic.
    """
    if current_user:
        clinic = crud.clinic.create(db=db, obj_in=clinic_in)
        return clinic
    else:
        raise HTTPException(
            status_code=404,
            detail="User does not have enough permissions",
        )


@router.patch("/clinic_id", response_model=schemas.Clinic)
def update_clinic(
    clinic_id: int,
    *,
    db: Session = Depends(deps.get_db),
    clinic_in: schemas.ClinicUpdate,
    current_user: models.db_tables.User = Depends(deps.get_current_active_user),
) -> Any:
    """
    Update clinic data.
    """
    if current_user:
        clinic = crud.clinic.get(db, id=clinic_id)
        if not clinic:
            raise HTTPException(
                status_code=404,
                detail="The clinic with this ID does not exist in the system",
            )
        clinic = crud.clinic.update(db=db, obj_in=clinic_in)
        return clinic
    else:
        raise HTTPException(
            status_code=404,
            detail="User does not have enough permissions",
        )




