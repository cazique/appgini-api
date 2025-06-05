from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.Encargo)
def create_encargo(
    *,
    db: Session = Depends(deps.get_db),
    encargo_in: schemas.EncargoCreate
) -> models.Encargo:
    """
    Create new encargo.
    """
    encargo = crud.crud_encargo.create(db=db, obj_in=encargo_in)
    return encargo

@router.get("/", response_model=List[schemas.Encargo])
def read_encargos(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve encargos.
    """
    encargos = crud.crud_encargo.get_multi(db, skip=skip, limit=limit)
    return encargos

@router.get("/{id}", response_model=schemas.Encargo)
def read_encargo(
    *,
    db: Session = Depends(deps.get_db),
    id: str
) -> models.Encargo:
    """
    Get encargo by id.
    """
    db_encargo = crud.crud_encargo.get(db=db, id=id)
    if not db_encargo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Encargo not found")
    return db_encargo

@router.put("/{id}", response_model=schemas.Encargo)
def update_encargo(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    encargo_in: schemas.EncargoUpdate
) -> models.Encargo:
    """
    Update encargo.
    """
    db_encargo = crud.crud_encargo.get(db=db, id=id)
    if not db_encargo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Encargo not found")
    encargo = crud.crud_encargo.update(db=db, db_obj=db_encargo, obj_in=encargo_in)
    return encargo

@router.delete("/{id}", response_model=schemas.Encargo)
def delete_encargo(
    *,
    db: Session = Depends(deps.get_db),
    id: str
) -> models.Encargo:
    """
    Delete a encargo.
    """
    db_encargo = crud.crud_encargo.get(db=db, id=id)
    if not db_encargo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Encargo not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_encargo = crud.crud_encargo.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_encargo is None and db_encargo is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting Encargo")
    return db_encargo # Return the object that was found by get, as per response_model
