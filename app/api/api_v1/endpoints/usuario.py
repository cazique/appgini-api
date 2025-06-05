from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.Usuario)
def create_usuario(
    *,
    db: Session = Depends(deps.get_db),
    usuario_in: schemas.UsuarioCreate
) -> models.Usuario:
    """
    Create new usuario.
    """
    usuario = crud.crud_usuario.create(db=db, obj_in=usuario_in)
    return usuario

@router.get("/", response_model=List[schemas.Usuario])
def read_usuarios(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve usuarios.
    """
    usuarios = crud.crud_usuario.get_multi(db, skip=skip, limit=limit)
    return usuarios

@router.get("/{id}", response_model=schemas.Usuario)
def read_usuario(
    *,
    db: Session = Depends(deps.get_db),
    id: str
) -> models.Usuario:
    """
    Get usuario by id.
    """
    db_usuario = crud.crud_usuario.get(db=db, id=id)
    if not db_usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario not found")
    return db_usuario

@router.put("/{id}", response_model=schemas.Usuario)
def update_usuario(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    usuario_in: schemas.UsuarioUpdate
) -> models.Usuario:
    """
    Update usuario.
    """
    db_usuario = crud.crud_usuario.get(db=db, id=id)
    if not db_usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario not found")
    usuario = crud.crud_usuario.update(db=db, db_obj=db_usuario, obj_in=usuario_in)
    return usuario

@router.delete("/{id}", response_model=schemas.Usuario)
def delete_usuario(
    *,
    db: Session = Depends(deps.get_db),
    id: str
) -> models.Usuario:
    """
    Delete a usuario.
    """
    db_usuario = crud.crud_usuario.get(db=db, id=id)
    if not db_usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_usuario = crud.crud_usuario.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_usuario is None and db_usuario is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting Usuario")
    return db_usuario # Return the object that was found by get, as per response_model
