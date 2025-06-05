from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.TipoProcedencia)
def create_tipo_procedencia(
    *,
    db: Session = Depends(deps.get_db),
    tipo_procedencia_in: schemas.TipoProcedenciaCreate
) -> models.TipoProcedencia:
    """
    Create new tipo_procedencia.
    """
    tipo_procedencia = crud.crud_tipo_procedencia.create(db=db, obj_in=tipo_procedencia_in)
    return tipo_procedencia

@router.get("/", response_model=List[schemas.TipoProcedencia])
def read_tipo_procedencias(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve tipo_procedencias.
    """
    tipo_procedencias = crud.crud_tipo_procedencia.get_multi(db, skip=skip, limit=limit)
    return tipo_procedencias

@router.get("/{id}", response_model=schemas.TipoProcedencia)
def read_tipo_procedencia(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.TipoProcedencia:
    """
    Get tipo_procedencia by id.
    """
    db_tipo_procedencia = crud.crud_tipo_procedencia.get(db=db, id=id)
    if not db_tipo_procedencia:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TipoProcedencia not found")
    return db_tipo_procedencia

@router.put("/{id}", response_model=schemas.TipoProcedencia)
def update_tipo_procedencia(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    tipo_procedencia_in: schemas.TipoProcedenciaUpdate
) -> models.TipoProcedencia:
    """
    Update tipo_procedencia.
    """
    db_tipo_procedencia = crud.crud_tipo_procedencia.get(db=db, id=id)
    if not db_tipo_procedencia:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TipoProcedencia not found")
    tipo_procedencia = crud.crud_tipo_procedencia.update(db=db, db_obj=db_tipo_procedencia, obj_in=tipo_procedencia_in)
    return tipo_procedencia

@router.delete("/{id}", response_model=schemas.TipoProcedencia)
def delete_tipo_procedencia(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.TipoProcedencia:
    """
    Delete a tipo_procedencia.
    """
    db_tipo_procedencia = crud.crud_tipo_procedencia.get(db=db, id=id)
    if not db_tipo_procedencia:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TipoProcedencia not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_tipo_procedencia = crud.crud_tipo_procedencia.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_tipo_procedencia is None and db_tipo_procedencia is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting TipoProcedencia")
    return db_tipo_procedencia # Return the object that was found by get, as per response_model
