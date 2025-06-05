from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.DetalleProcedencia)
def create_detalle_procedencia(
    *,
    db: Session = Depends(deps.get_db),
    detalle_procedencia_in: schemas.DetalleProcedenciaCreate
) -> models.DetalleProcedencia:
    """
    Create new detalle_procedencia.
    """
    detalle_procedencia = crud.crud_detalle_procedencia.create(db=db, obj_in=detalle_procedencia_in)
    return detalle_procedencia

@router.get("/", response_model=List[schemas.DetalleProcedencia])
def read_detalle_procedencias(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve detalle_procedencias.
    """
    detalle_procedencias = crud.crud_detalle_procedencia.get_multi(db, skip=skip, limit=limit)
    return detalle_procedencias

@router.get("/{id}", response_model=schemas.DetalleProcedencia)
def read_detalle_procedencia(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.DetalleProcedencia:
    """
    Get detalle_procedencia by id.
    """
    db_detalle_procedencia = crud.crud_detalle_procedencia.get(db=db, id=id)
    if not db_detalle_procedencia:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="DetalleProcedencia not found")
    return db_detalle_procedencia

@router.put("/{id}", response_model=schemas.DetalleProcedencia)
def update_detalle_procedencia(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    detalle_procedencia_in: schemas.DetalleProcedenciaUpdate
) -> models.DetalleProcedencia:
    """
    Update detalle_procedencia.
    """
    db_detalle_procedencia = crud.crud_detalle_procedencia.get(db=db, id=id)
    if not db_detalle_procedencia:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="DetalleProcedencia not found")
    detalle_procedencia = crud.crud_detalle_procedencia.update(db=db, db_obj=db_detalle_procedencia, obj_in=detalle_procedencia_in)
    return detalle_procedencia

@router.delete("/{id}", response_model=schemas.DetalleProcedencia)
def delete_detalle_procedencia(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.DetalleProcedencia:
    """
    Delete a detalle_procedencia.
    """
    db_detalle_procedencia = crud.crud_detalle_procedencia.get(db=db, id=id)
    if not db_detalle_procedencia:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="DetalleProcedencia not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_detalle_procedencia = crud.crud_detalle_procedencia.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_detalle_procedencia is None and db_detalle_procedencia is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting DetalleProcedencia")
    return db_detalle_procedencia # Return the object that was found by get, as per response_model
