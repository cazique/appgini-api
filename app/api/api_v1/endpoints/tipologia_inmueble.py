from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.TipologiaInmueble)
def create_tipologia_inmueble(
    *,
    db: Session = Depends(deps.get_db),
    tipologia_inmueble_in: schemas.TipologiaInmuebleCreate
) -> models.TipologiaInmueble:
    """
    Create new tipologia_inmueble.
    """
    tipologia_inmueble = crud.crud_tipologia_inmueble.create(db=db, obj_in=tipologia_inmueble_in)
    return tipologia_inmueble

@router.get("/", response_model=List[schemas.TipologiaInmueble])
def read_tipologia_inmuebles(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve tipologia_inmuebles.
    """
    tipologia_inmuebles = crud.crud_tipologia_inmueble.get_multi(db, skip=skip, limit=limit)
    return tipologia_inmuebles

@router.get("/{id}", response_model=schemas.TipologiaInmueble)
def read_tipologia_inmueble(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.TipologiaInmueble:
    """
    Get tipologia_inmueble by id.
    """
    db_tipologia_inmueble = crud.crud_tipologia_inmueble.get(db=db, id=id)
    if not db_tipologia_inmueble:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TipologiaInmueble not found")
    return db_tipologia_inmueble

@router.put("/{id}", response_model=schemas.TipologiaInmueble)
def update_tipologia_inmueble(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    tipologia_inmueble_in: schemas.TipologiaInmuebleUpdate
) -> models.TipologiaInmueble:
    """
    Update tipologia_inmueble.
    """
    db_tipologia_inmueble = crud.crud_tipologia_inmueble.get(db=db, id=id)
    if not db_tipologia_inmueble:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TipologiaInmueble not found")
    tipologia_inmueble = crud.crud_tipologia_inmueble.update(db=db, db_obj=db_tipologia_inmueble, obj_in=tipologia_inmueble_in)
    return tipologia_inmueble

@router.delete("/{id}", response_model=schemas.TipologiaInmueble)
def delete_tipologia_inmueble(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.TipologiaInmueble:
    """
    Delete a tipologia_inmueble.
    """
    db_tipologia_inmueble = crud.crud_tipologia_inmueble.get(db=db, id=id)
    if not db_tipologia_inmueble:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TipologiaInmueble not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_tipologia_inmueble = crud.crud_tipologia_inmueble.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_tipologia_inmueble is None and db_tipologia_inmueble is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting TipologiaInmueble")
    return db_tipologia_inmueble # Return the object that was found by get, as per response_model
