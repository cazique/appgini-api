from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.Prioridad)
def create_prioridad(
    *,
    db: Session = Depends(deps.get_db),
    prioridad_in: schemas.PrioridadCreate
) -> models.Prioridad:
    """
    Create new prioridad.
    """
    prioridad = crud.crud_prioridad.create(db=db, obj_in=prioridad_in)
    return prioridad

@router.get("/", response_model=List[schemas.Prioridad])
def read_prioridads(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve prioridads.
    """
    prioridads = crud.crud_prioridad.get_multi(db, skip=skip, limit=limit)
    return prioridads

@router.get("/{id}", response_model=schemas.Prioridad)
def read_prioridad(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.Prioridad:
    """
    Get prioridad by id.
    """
    db_prioridad = crud.crud_prioridad.get(db=db, id=id)
    if not db_prioridad:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prioridad not found")
    return db_prioridad

@router.put("/{id}", response_model=schemas.Prioridad)
def update_prioridad(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    prioridad_in: schemas.PrioridadUpdate
) -> models.Prioridad:
    """
    Update prioridad.
    """
    db_prioridad = crud.crud_prioridad.get(db=db, id=id)
    if not db_prioridad:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prioridad not found")
    prioridad = crud.crud_prioridad.update(db=db, db_obj=db_prioridad, obj_in=prioridad_in)
    return prioridad

@router.delete("/{id}", response_model=schemas.Prioridad)
def delete_prioridad(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.Prioridad:
    """
    Delete a prioridad.
    """
    db_prioridad = crud.crud_prioridad.get(db=db, id=id)
    if not db_prioridad:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prioridad not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_prioridad = crud.crud_prioridad.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_prioridad is None and db_prioridad is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting Prioridad")
    return db_prioridad # Return the object that was found by get, as per response_model
