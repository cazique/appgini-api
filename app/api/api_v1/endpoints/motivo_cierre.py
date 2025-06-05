from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.MotivoCierre)
def create_motivo_cierre(
    *,
    db: Session = Depends(deps.get_db),
    motivo_cierre_in: schemas.MotivoCierreCreate
) -> models.MotivoCierre:
    """
    Create new motivo_cierre.
    """
    motivo_cierre = crud.crud_motivo_cierre.create(db=db, obj_in=motivo_cierre_in)
    return motivo_cierre

@router.get("/", response_model=List[schemas.MotivoCierre])
def read_motivo_cierres(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve motivo_cierres.
    """
    motivo_cierres = crud.crud_motivo_cierre.get_multi(db, skip=skip, limit=limit)
    return motivo_cierres

@router.get("/{id}", response_model=schemas.MotivoCierre)
def read_motivo_cierre(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.MotivoCierre:
    """
    Get motivo_cierre by id.
    """
    db_motivo_cierre = crud.crud_motivo_cierre.get(db=db, id=id)
    if not db_motivo_cierre:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MotivoCierre not found")
    return db_motivo_cierre

@router.put("/{id}", response_model=schemas.MotivoCierre)
def update_motivo_cierre(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    motivo_cierre_in: schemas.MotivoCierreUpdate
) -> models.MotivoCierre:
    """
    Update motivo_cierre.
    """
    db_motivo_cierre = crud.crud_motivo_cierre.get(db=db, id=id)
    if not db_motivo_cierre:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MotivoCierre not found")
    motivo_cierre = crud.crud_motivo_cierre.update(db=db, db_obj=db_motivo_cierre, obj_in=motivo_cierre_in)
    return motivo_cierre

@router.delete("/{id}", response_model=schemas.MotivoCierre)
def delete_motivo_cierre(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.MotivoCierre:
    """
    Delete a motivo_cierre.
    """
    db_motivo_cierre = crud.crud_motivo_cierre.get(db=db, id=id)
    if not db_motivo_cierre:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MotivoCierre not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_motivo_cierre = crud.crud_motivo_cierre.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_motivo_cierre is None and db_motivo_cierre is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting MotivoCierre")
    return db_motivo_cierre # Return the object that was found by get, as per response_model
