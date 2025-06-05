from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.Inmueble)
def create_inmueble(
    *,
    db: Session = Depends(deps.get_db),
    inmueble_in: schemas.InmuebleCreate
) -> models.Inmueble:
    """
    Create new inmueble.
    """
    inmueble = crud.crud_inmueble.create(db=db, obj_in=inmueble_in)
    return inmueble

@router.get("/", response_model=List[schemas.Inmueble])
def read_inmuebles(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve inmuebles.
    """
    inmuebles = crud.crud_inmueble.get_multi(db, skip=skip, limit=limit)
    return inmuebles

@router.get("/{id}", response_model=schemas.Inmueble)
def read_inmueble(
    *,
    db: Session = Depends(deps.get_db),
    id: str
) -> models.Inmueble:
    """
    Get inmueble by id.
    """
    db_inmueble = crud.crud_inmueble.get(db=db, id=id)
    if not db_inmueble:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inmueble not found")
    return db_inmueble

@router.put("/{id}", response_model=schemas.Inmueble)
def update_inmueble(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    inmueble_in: schemas.InmuebleUpdate
) -> models.Inmueble:
    """
    Update inmueble.
    """
    db_inmueble = crud.crud_inmueble.get(db=db, id=id)
    if not db_inmueble:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inmueble not found")
    inmueble = crud.crud_inmueble.update(db=db, db_obj=db_inmueble, obj_in=inmueble_in)
    return inmueble

@router.delete("/{id}", response_model=schemas.Inmueble)
def delete_inmueble(
    *,
    db: Session = Depends(deps.get_db),
    id: str
) -> models.Inmueble:
    """
    Delete a inmueble.
    """
    db_inmueble = crud.crud_inmueble.get(db=db, id=id)
    if not db_inmueble:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Inmueble not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_inmueble = crud.crud_inmueble.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_inmueble is None and db_inmueble is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting Inmueble")
    return db_inmueble # Return the object that was found by get, as per response_model
