from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.EstadoNoticia)
def create_estado_noticia(
    *,
    db: Session = Depends(deps.get_db),
    estado_noticia_in: schemas.EstadoNoticiaCreate
) -> models.EstadoNoticia:
    """
    Create new estado_noticia.
    """
    estado_noticia = crud.crud_estado_noticia.create(db=db, obj_in=estado_noticia_in)
    return estado_noticia

@router.get("/", response_model=List[schemas.EstadoNoticia])
def read_estado_noticias(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve estado_noticias.
    """
    estado_noticias = crud.crud_estado_noticia.get_multi(db, skip=skip, limit=limit)
    return estado_noticias

@router.get("/{id}", response_model=schemas.EstadoNoticia)
def read_estado_noticia(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.EstadoNoticia:
    """
    Get estado_noticia by id.
    """
    db_estado_noticia = crud.crud_estado_noticia.get(db=db, id=id)
    if not db_estado_noticia:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EstadoNoticia not found")
    return db_estado_noticia

@router.put("/{id}", response_model=schemas.EstadoNoticia)
def update_estado_noticia(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    estado_noticia_in: schemas.EstadoNoticiaUpdate
) -> models.EstadoNoticia:
    """
    Update estado_noticia.
    """
    db_estado_noticia = crud.crud_estado_noticia.get(db=db, id=id)
    if not db_estado_noticia:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EstadoNoticia not found")
    estado_noticia = crud.crud_estado_noticia.update(db=db, db_obj=db_estado_noticia, obj_in=estado_noticia_in)
    return estado_noticia

@router.delete("/{id}", response_model=schemas.EstadoNoticia)
def delete_estado_noticia(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.EstadoNoticia:
    """
    Delete a estado_noticia.
    """
    db_estado_noticia = crud.crud_estado_noticia.get(db=db, id=id)
    if not db_estado_noticia:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="EstadoNoticia not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_estado_noticia = crud.crud_estado_noticia.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_estado_noticia is None and db_estado_noticia is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting EstadoNoticia")
    return db_estado_noticia # Return the object that was found by get, as per response_model
