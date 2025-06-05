from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.EstadoEncargo)
def create_estado_encargo(
    *,
    db: Session = Depends(deps.get_db),
    estado_encargo_in: schemas.EstadoEncargoCreate
) -> models.EstadoEncargo:
    """
    Create new estado_encargo.
    """
    estado_encargo = crud.crud_estado_encargo.create(db=db, obj_in=estado_encargo_in)
    return estado_encargo

@router.get("/", response_model=List[schemas.EstadoEncargo])
def read_estado_encargos(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve estado_encargos.
    """
    estado_encargos = crud.crud_estado_encargo.get_multi(db, skip=skip, limit=limit)
    return estado_encargos

@router.get("/{id}", response_model=schemas.EstadoEncargo)
def read_estado_encargo(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.EstadoEncargo:
    """
    Get estado_encargo by id.
    """
    db_estado_encargo = crud.crud_estado_encargo.get(db=db, id=id)
    if not db_estado_encargo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EstadoEncargo not found")
    return db_estado_encargo

@router.put("/{id}", response_model=schemas.EstadoEncargo)
def update_estado_encargo(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    estado_encargo_in: schemas.EstadoEncargoUpdate
) -> models.EstadoEncargo:
    """
    Update estado_encargo.
    """
    db_estado_encargo = crud.crud_estado_encargo.get(db=db, id=id)
    if not db_estado_encargo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EstadoEncargo not found")
    estado_encargo = crud.crud_estado_encargo.update(db=db, db_obj=db_estado_encargo, obj_in=estado_encargo_in)
    return estado_encargo

@router.delete("/{id}", response_model=schemas.EstadoEncargo)
def delete_estado_encargo(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.EstadoEncargo:
    """
    Delete a estado_encargo.
    """
    db_estado_encargo = crud.crud_estado_encargo.get(db=db, id=id)
    if not db_estado_encargo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EstadoEncargo not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_estado_encargo = crud.crud_estado_encargo.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_estado_encargo is None and db_estado_encargo is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting EstadoEncargo")
    return db_estado_encargo # Return the object that was found by get, as per response_model
