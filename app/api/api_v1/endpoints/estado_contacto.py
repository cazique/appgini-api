from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.EstadoContacto)
def create_estado_contacto(
    *,
    db: Session = Depends(deps.get_db),
    estado_contacto_in: schemas.EstadoContactoCreate
) -> models.EstadoContacto:
    """
    Create new estado_contacto.
    """
    estado_contacto = crud.crud_estado_contacto.create(db=db, obj_in=estado_contacto_in)
    return estado_contacto

@router.get("/", response_model=List[schemas.EstadoContacto])
def read_estado_contactos(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve estado_contactos.
    """
    estado_contactos = crud.crud_estado_contacto.get_multi(db, skip=skip, limit=limit)
    return estado_contactos

@router.get("/{id}", response_model=schemas.EstadoContacto)
def read_estado_contacto(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.EstadoContacto:
    """
    Get estado_contacto by id.
    """
    db_estado_contacto = crud.crud_estado_contacto.get(db=db, id=id)
    if not db_estado_contacto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EstadoContacto not found")
    return db_estado_contacto

@router.put("/{id}", response_model=schemas.EstadoContacto)
def update_estado_contacto(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    estado_contacto_in: schemas.EstadoContactoUpdate
) -> models.EstadoContacto:
    """
    Update estado_contacto.
    """
    db_estado_contacto = crud.crud_estado_contacto.get(db=db, id=id)
    if not db_estado_contacto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EstadoContacto not found")
    estado_contacto = crud.crud_estado_contacto.update(db=db, db_obj=db_estado_contacto, obj_in=estado_contacto_in)
    return estado_contacto

@router.delete("/{id}", response_model=schemas.EstadoContacto)
def delete_estado_contacto(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.EstadoContacto:
    """
    Delete a estado_contacto.
    """
    db_estado_contacto = crud.crud_estado_contacto.get(db=db, id=id)
    if not db_estado_contacto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EstadoContacto not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_estado_contacto = crud.crud_estado_contacto.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_estado_contacto is None and db_estado_contacto is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting EstadoContacto")
    return db_estado_contacto # Return the object that was found by get, as per response_model
