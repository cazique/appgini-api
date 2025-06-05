from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.ActividadEncargo)
def create_actividad_encargo(
    *,
    db: Session = Depends(deps.get_db),
    actividad_encargo_in: schemas.ActividadEncargoCreate
) -> models.ActividadEncargo:
    """
    Create new actividad_encargo.
    """
    actividad_encargo = crud.crud_actividad_encargo.create(db=db, obj_in=actividad_encargo_in)
    return actividad_encargo

@router.get("/", response_model=List[schemas.ActividadEncargo])
def read_actividad_encargos(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve actividad_encargos.
    """
    actividad_encargos = crud.crud_actividad_encargo.get_multi(db, skip=skip, limit=limit)
    return actividad_encargos

@router.get("/{id}", response_model=schemas.ActividadEncargo)
def read_actividad_encargo(
    *,
    db: Session = Depends(deps.get_db),
    id: str
) -> models.ActividadEncargo:
    """
    Get actividad_encargo by id.
    """
    db_actividad_encargo = crud.crud_actividad_encargo.get(db=db, id=id)
    if not db_actividad_encargo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ActividadEncargo not found")
    return db_actividad_encargo

@router.put("/{id}", response_model=schemas.ActividadEncargo)
def update_actividad_encargo(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    actividad_encargo_in: schemas.ActividadEncargoUpdate
) -> models.ActividadEncargo:
    """
    Update actividad_encargo.
    """
    db_actividad_encargo = crud.crud_actividad_encargo.get(db=db, id=id)
    if not db_actividad_encargo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ActividadEncargo not found")
    actividad_encargo = crud.crud_actividad_encargo.update(db=db, db_obj=db_actividad_encargo, obj_in=actividad_encargo_in)
    return actividad_encargo

@router.delete("/{id}", response_model=schemas.ActividadEncargo)
def delete_actividad_encargo(
    *,
    db: Session = Depends(deps.get_db),
    id: str
) -> models.ActividadEncargo:
    """
    Delete a actividad_encargo.
    """
    db_actividad_encargo = crud.crud_actividad_encargo.get(db=db, id=id)
    if not db_actividad_encargo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ActividadEncargo not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_actividad_encargo = crud.crud_actividad_encargo.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_actividad_encargo is None and db_actividad_encargo is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting ActividadEncargo")
    return db_actividad_encargo # Return the object that was found by get, as per response_model
