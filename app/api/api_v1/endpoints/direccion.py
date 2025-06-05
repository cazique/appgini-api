from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.Direccion)
def create_direccion(
    *,
    db: Session = Depends(deps.get_db),
    direccion_in: schemas.DireccionCreate
) -> models.Direccion:
    """
    Create new direccion.
    """
    direccion = crud.crud_direccion.create(db=db, obj_in=direccion_in)
    return direccion

@router.get("/", response_model=List[schemas.Direccion])
def read_direccions(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve direccions.
    """
    direccions = crud.crud_direccion.get_multi(db, skip=skip, limit=limit)
    return direccions

@router.get("/{id}", response_model=schemas.Direccion)
def read_direccion(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.Direccion:
    """
    Get direccion by id.
    """
    db_direccion = crud.crud_direccion.get(db=db, id=id)
    if not db_direccion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Direccion not found")
    return db_direccion

@router.put("/{id}", response_model=schemas.Direccion)
def update_direccion(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    direccion_in: schemas.DireccionUpdate
) -> models.Direccion:
    """
    Update direccion.
    """
    db_direccion = crud.crud_direccion.get(db=db, id=id)
    if not db_direccion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Direccion not found")
    direccion = crud.crud_direccion.update(db=db, db_obj=db_direccion, obj_in=direccion_in)
    return direccion

@router.delete("/{id}", response_model=schemas.Direccion)
def delete_direccion(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.Direccion:
    """
    Delete a direccion.
    """
    db_direccion = crud.crud_direccion.get(db=db, id=id)
    if not db_direccion:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Direccion not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_direccion = crud.crud_direccion.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_direccion is None and db_direccion is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting Direccion")
    return db_direccion # Return the object that was found by get, as per response_model
