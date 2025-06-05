from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.Subzona)
def create_subzona(
    *,
    db: Session = Depends(deps.get_db),
    subzona_in: schemas.SubzonaCreate
) -> models.Subzona:
    """
    Create new subzona.
    """
    subzona = crud.crud_subzona.create(db=db, obj_in=subzona_in)
    return subzona

@router.get("/", response_model=List[schemas.Subzona])
def read_subzonas(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve subzonas.
    """
    subzonas = crud.crud_subzona.get_multi(db, skip=skip, limit=limit)
    return subzonas

@router.get("/{id}", response_model=schemas.Subzona)
def read_subzona(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.Subzona:
    """
    Get subzona by id.
    """
    db_subzona = crud.crud_subzona.get(db=db, id=id)
    if not db_subzona:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Subzona not found")
    return db_subzona

@router.put("/{id}", response_model=schemas.Subzona)
def update_subzona(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    subzona_in: schemas.SubzonaUpdate
) -> models.Subzona:
    """
    Update subzona.
    """
    db_subzona = crud.crud_subzona.get(db=db, id=id)
    if not db_subzona:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Subzona not found")
    subzona = crud.crud_subzona.update(db=db, db_obj=db_subzona, obj_in=subzona_in)
    return subzona

@router.delete("/{id}", response_model=schemas.Subzona)
def delete_subzona(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.Subzona:
    """
    Delete a subzona.
    """
    db_subzona = crud.crud_subzona.get(db=db, id=id)
    if not db_subzona:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Subzona not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_subzona = crud.crud_subzona.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_subzona is None and db_subzona is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting Subzona")
    return db_subzona # Return the object that was found by get, as per response_model
