from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.ModalidadContacto)
def create_modalidad_contacto(
    *,
    db: Session = Depends(deps.get_db),
    modalidad_contacto_in: schemas.ModalidadContactoCreate
) -> models.ModalidadContacto:
    """
    Create new modalidad_contacto.
    """
    modalidad_contacto = crud.crud_modalidad_contacto.create(db=db, obj_in=modalidad_contacto_in)
    return modalidad_contacto

@router.get("/", response_model=List[schemas.ModalidadContacto])
def read_modalidad_contactos(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve modalidad_contactos.
    """
    modalidad_contactos = crud.crud_modalidad_contacto.get_multi(db, skip=skip, limit=limit)
    return modalidad_contactos

@router.get("/{id}", response_model=schemas.ModalidadContacto)
def read_modalidad_contacto(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.ModalidadContacto:
    """
    Get modalidad_contacto by id.
    """
    db_modalidad_contacto = crud.crud_modalidad_contacto.get(db=db, id=id)
    if not db_modalidad_contacto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ModalidadContacto not found")
    return db_modalidad_contacto

@router.put("/{id}", response_model=schemas.ModalidadContacto)
def update_modalidad_contacto(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    modalidad_contacto_in: schemas.ModalidadContactoUpdate
) -> models.ModalidadContacto:
    """
    Update modalidad_contacto.
    """
    db_modalidad_contacto = crud.crud_modalidad_contacto.get(db=db, id=id)
    if not db_modalidad_contacto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ModalidadContacto not found")
    modalidad_contacto = crud.crud_modalidad_contacto.update(db=db, db_obj=db_modalidad_contacto, obj_in=modalidad_contacto_in)
    return modalidad_contacto

@router.delete("/{id}", response_model=schemas.ModalidadContacto)
def delete_modalidad_contacto(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.ModalidadContacto:
    """
    Delete a modalidad_contacto.
    """
    db_modalidad_contacto = crud.crud_modalidad_contacto.get(db=db, id=id)
    if not db_modalidad_contacto:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ModalidadContacto not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_modalidad_contacto = crud.crud_modalidad_contacto.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_modalidad_contacto is None and db_modalidad_contacto is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting ModalidadContacto")
    return db_modalidad_contacto # Return the object that was found by get, as per response_model
