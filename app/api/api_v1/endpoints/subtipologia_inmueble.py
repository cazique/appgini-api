from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.SubtipologiaInmueble)
def create_subtipologia_inmueble(
    *,
    db: Session = Depends(deps.get_db),
    subtipologia_inmueble_in: schemas.SubtipologiaInmuebleCreate
) -> models.SubtipologiaInmueble:
    """
    Create new subtipologia_inmueble.
    """
    subtipologia_inmueble = crud.crud_subtipologia_inmueble.create(db=db, obj_in=subtipologia_inmueble_in)
    return subtipologia_inmueble

@router.get("/", response_model=List[schemas.SubtipologiaInmueble])
def read_subtipologia_inmuebles(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve subtipologia_inmuebles.
    """
    subtipologia_inmuebles = crud.crud_subtipologia_inmueble.get_multi(db, skip=skip, limit=limit)
    return subtipologia_inmuebles

@router.get("/{id}", response_model=schemas.SubtipologiaInmueble)
def read_subtipologia_inmueble(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.SubtipologiaInmueble:
    """
    Get subtipologia_inmueble by id.
    """
    db_subtipologia_inmueble = crud.crud_subtipologia_inmueble.get(db=db, id=id)
    if not db_subtipologia_inmueble:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="SubtipologiaInmueble not found")
    return db_subtipologia_inmueble

@router.put("/{id}", response_model=schemas.SubtipologiaInmueble)
def update_subtipologia_inmueble(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    subtipologia_inmueble_in: schemas.SubtipologiaInmuebleUpdate
) -> models.SubtipologiaInmueble:
    """
    Update subtipologia_inmueble.
    """
    db_subtipologia_inmueble = crud.crud_subtipologia_inmueble.get(db=db, id=id)
    if not db_subtipologia_inmueble:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="SubtipologiaInmueble not found")
    subtipologia_inmueble = crud.crud_subtipologia_inmueble.update(db=db, db_obj=db_subtipologia_inmueble, obj_in=subtipologia_inmueble_in)
    return subtipologia_inmueble

@router.delete("/{id}", response_model=schemas.SubtipologiaInmueble)
def delete_subtipologia_inmueble(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.SubtipologiaInmueble:
    """
    Delete a subtipologia_inmueble.
    """
    db_subtipologia_inmueble = crud.crud_subtipologia_inmueble.get(db=db, id=id)
    if not db_subtipologia_inmueble:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="SubtipologiaInmueble not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_subtipologia_inmueble = crud.crud_subtipologia_inmueble.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_subtipologia_inmueble is None and db_subtipologia_inmueble is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting SubtipologiaInmueble")
    return db_subtipologia_inmueble # Return the object that was found by get, as per response_model
