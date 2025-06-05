from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.Actividad)
def create_actividad(
    *,
    db: Session = Depends(deps.get_db),
    actividad_in: schemas.ActividadCreate
) -> models.Actividad:
    """
    Create new actividad.
    """
    actividad = crud.crud_actividad.create(db=db, obj_in=actividad_in)
    return actividad

@router.get("/", response_model=List[schemas.Actividad])
def read_actividads(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve actividads.
    """
    actividads = crud.crud_actividad.get_multi(db, skip=skip, limit=limit)
    return actividads

@router.get("/{id}", response_model=schemas.Actividad)
def read_actividad(
    *,
    db: Session = Depends(deps.get_db),
    id: str
) -> models.Actividad:
    """
    Get actividad by id.
    """
    db_actividad = crud.crud_actividad.get(db=db, id=id)
    if not db_actividad:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Actividad not found")
    return db_actividad

@router.put("/{id}", response_model=schemas.Actividad)
def update_actividad(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    actividad_in: schemas.ActividadUpdate
) -> models.Actividad:
    """
    Update actividad.
    """
    db_actividad = crud.crud_actividad.get(db=db, id=id)
    if not db_actividad:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Actividad not found")
    actividad = crud.crud_actividad.update(db=db, db_obj=db_actividad, obj_in=actividad_in)
    return actividad

@router.delete("/{id}", response_model=schemas.Actividad)
def delete_actividad(
    *,
    db: Session = Depends(deps.get_db),
    id: str
) -> models.Actividad:
    """
    Delete a actividad.
    """
    db_actividad = crud.crud_actividad.get(db=db, id=id)
    if not db_actividad:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Actividad not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_actividad = crud.crud_actividad.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_actividad is None and db_actividad is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting Actividad")
    return db_actividad # Return the object that was found by get, as per response_model
