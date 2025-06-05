from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.Zona)
def create_zona(
    *,
    db: Session = Depends(deps.get_db),
    zona_in: schemas.ZonaCreate
) -> models.Zona:
    """
    Create new zona.
    """
    zona = crud.crud_zona.create(db=db, obj_in=zona_in)
    return zona

@router.get("/", response_model=List[schemas.Zona])
def read_zonas(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve zonas.
    """
    zonas = crud.crud_zona.get_multi(db, skip=skip, limit=limit)
    return zonas

@router.get("/{id}", response_model=schemas.Zona)
def read_zona(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.Zona:
    """
    Get zona by id.
    """
    db_zona = crud.crud_zona.get(db=db, id=id)
    if not db_zona:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Zona not found")
    return db_zona

@router.put("/{id}", response_model=schemas.Zona)
def update_zona(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    zona_in: schemas.ZonaUpdate
) -> models.Zona:
    """
    Update zona.
    """
    db_zona = crud.crud_zona.get(db=db, id=id)
    if not db_zona:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Zona not found")
    zona = crud.crud_zona.update(db=db, db_obj=db_zona, obj_in=zona_in)
    return zona

@router.delete("/{id}", response_model=schemas.Zona)
def delete_zona(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.Zona:
    """
    Delete a zona.
    """
    db_zona = crud.crud_zona.get(db=db, id=id)
    if not db_zona:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Zona not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_zona = crud.crud_zona.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_zona is None and db_zona is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting Zona")
    return db_zona # Return the object that was found by get, as per response_model
