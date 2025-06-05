from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.Noticia)
def create_noticia(
    *,
    db: Session = Depends(deps.get_db),
    noticia_in: schemas.NoticiaCreate
) -> models.Noticia:
    """
    Create new noticia.
    """
    noticia = crud.crud_noticia.create(db=db, obj_in=noticia_in)
    return noticia

@router.get("/", response_model=List[schemas.Noticia])
def read_noticias(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve noticias.
    """
    noticias = crud.crud_noticia.get_multi(db, skip=skip, limit=limit)
    return noticias

@router.get("/{id}", response_model=schemas.Noticia)
def read_noticia(
    *,
    db: Session = Depends(deps.get_db),
    id: str
) -> models.Noticia:
    """
    Get noticia by id.
    """
    db_noticia = crud.crud_noticia.get(db=db, id=id)
    if not db_noticia:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Noticia not found")
    return db_noticia

@router.put("/{id}", response_model=schemas.Noticia)
def update_noticia(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    noticia_in: schemas.NoticiaUpdate
) -> models.Noticia:
    """
    Update noticia.
    """
    db_noticia = crud.crud_noticia.get(db=db, id=id)
    if not db_noticia:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Noticia not found")
    noticia = crud.crud_noticia.update(db=db, db_obj=db_noticia, obj_in=noticia_in)
    return noticia

@router.delete("/{id}", response_model=schemas.Noticia)
def delete_noticia(
    *,
    db: Session = Depends(deps.get_db),
    id: str
) -> models.Noticia:
    """
    Delete a noticia.
    """
    db_noticia = crud.crud_noticia.get(db=db, id=id)
    if not db_noticia:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Noticia not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_noticia = crud.crud_noticia.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_noticia is None and db_noticia is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting Noticia")
    return db_noticia # Return the object that was found by get, as per response_model
