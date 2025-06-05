from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.Cliente)
def create_cliente(
    *,
    db: Session = Depends(deps.get_db),
    cliente_in: schemas.ClienteCreate
) -> models.Cliente:
    """
    Create new cliente.
    """
    cliente = crud.crud_cliente.create(db=db, obj_in=cliente_in)
    return cliente

@router.get("/", response_model=List[schemas.Cliente])
def read_clientes(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve clientes.
    """
    clientes = crud.crud_cliente.get_multi(db, skip=skip, limit=limit)
    return clientes

@router.get("/{id}", response_model=schemas.Cliente)
def read_cliente(
    *,
    db: Session = Depends(deps.get_db),
    id: str
) -> models.Cliente:
    """
    Get cliente by id.
    """
    db_cliente = crud.crud_cliente.get(db=db, id=id)
    if not db_cliente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente not found")
    return db_cliente

@router.put("/{id}", response_model=schemas.Cliente)
def update_cliente(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    cliente_in: schemas.ClienteUpdate
) -> models.Cliente:
    """
    Update cliente.
    """
    db_cliente = crud.crud_cliente.get(db=db, id=id)
    if not db_cliente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente not found")
    cliente = crud.crud_cliente.update(db=db, db_obj=db_cliente, obj_in=cliente_in)
    return cliente

@router.delete("/{id}", response_model=schemas.Cliente)
def delete_cliente(
    *,
    db: Session = Depends(deps.get_db),
    id: str
) -> models.Cliente:
    """
    Delete a cliente.
    """
    db_cliente = crud.crud_cliente.get(db=db, id=id)
    if not db_cliente:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_cliente = crud.crud_cliente.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_cliente is None and db_cliente is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting Cliente")
    return db_cliente # Return the object that was found by get, as per response_model
