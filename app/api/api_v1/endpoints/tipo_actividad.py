from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.TipoActividad)
def create_tipo_actividad(
    *,
    db: Session = Depends(deps.get_db),
    tipo_actividad_in: schemas.TipoActividadCreate
) -> models.TipoActividad:
    """
    Create new tipo_actividad.
    """
    tipo_actividad = crud.crud_tipo_actividad.create(db=db, obj_in=tipo_actividad_in)
    return tipo_actividad

@router.get("/", response_model=List[schemas.TipoActividad])
def read_tipo_actividads(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve tipo_actividads.
    """
    tipo_actividads = crud.crud_tipo_actividad.get_multi(db, skip=skip, limit=limit)
    return tipo_actividads

@router.get("/{id}", response_model=schemas.TipoActividad)
def read_tipo_actividad(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.TipoActividad:
    """
    Get tipo_actividad by id.
    """
    db_tipo_actividad = crud.crud_tipo_actividad.get(db=db, id=id)
    if not db_tipo_actividad:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TipoActividad not found")
    return db_tipo_actividad

@router.put("/{id}", response_model=schemas.TipoActividad)
def update_tipo_actividad(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    tipo_actividad_in: schemas.TipoActividadUpdate
) -> models.TipoActividad:
    """
    Update tipo_actividad.
    """
    db_tipo_actividad = crud.crud_tipo_actividad.get(db=db, id=id)
    if not db_tipo_actividad:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TipoActividad not found")
    tipo_actividad = crud.crud_tipo_actividad.update(db=db, db_obj=db_tipo_actividad, obj_in=tipo_actividad_in)
    return tipo_actividad

@router.delete("/{id}", response_model=schemas.TipoActividad)
def delete_tipo_actividad(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.TipoActividad:
    """
    Delete a tipo_actividad.
    """
    db_tipo_actividad = crud.crud_tipo_actividad.get(db=db, id=id)
    if not db_tipo_actividad:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TipoActividad not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_tipo_actividad = crud.crud_tipo_actividad.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_tipo_actividad is None and db_tipo_actividad is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting TipoActividad")
    return db_tipo_actividad # Return the object that was found by get, as per response_model
