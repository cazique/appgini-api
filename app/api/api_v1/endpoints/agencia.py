from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.Agencia)
def create_agencia(
    *,
    db: Session = Depends(deps.get_db),
    agencia_in: schemas.AgenciaCreate
) -> models.Agencia:
    """
    Create new agencia.
    """
    agencia = crud.crud_agencia.create(db=db, obj_in=agencia_in)
    return agencia

@router.get("/", response_model=List[schemas.Agencia])
def read_agencias(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve agencias.
    """
    agencias = crud.crud_agencia.get_multi(db, skip=skip, limit=limit)
    return agencias

@router.get("/{id}", response_model=schemas.Agencia)
def read_agencia(
    *,
    db: Session = Depends(deps.get_db),
    id: str
) -> models.Agencia:
    """
    Get agencia by id.
    """
    db_agencia = crud.crud_agencia.get(db=db, id=id)
    if not db_agencia:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Agencia not found")
    return db_agencia

@router.put("/{id}", response_model=schemas.Agencia)
def update_agencia(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    agencia_in: schemas.AgenciaUpdate
) -> models.Agencia:
    """
    Update agencia.
    """
    db_agencia = crud.crud_agencia.get(db=db, id=id)
    if not db_agencia:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Agencia not found")
    agencia = crud.crud_agencia.update(db=db, db_obj=db_agencia, obj_in=agencia_in)
    return agencia

@router.delete("/{id}", response_model=schemas.Agencia)
def delete_agencia(
    *,
    db: Session = Depends(deps.get_db),
    id: str
) -> models.Agencia:
    """
    Delete a agencia.
    """
    db_agencia = crud.crud_agencia.get(db=db, id=id)
    if not db_agencia:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Agencia not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_agencia = crud.crud_agencia.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_agencia is None and db_agencia is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting Agencia")
    return db_agencia # Return the object that was found by get, as per response_model
