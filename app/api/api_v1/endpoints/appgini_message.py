from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.AppginiMessage)
def create_appgini_message(
    *,
    db: Session = Depends(deps.get_db),
    appgini_message_in: schemas.AppginiMessageCreate
) -> models.AppginiMessage:
    """
    Create new appgini_message.
    """
    appgini_message = crud.crud_appgini_message.create(db=db, obj_in=appgini_message_in)
    return appgini_message

@router.get("/", response_model=List[schemas.AppginiMessage])
def read_appgini_messages(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve appgini_messages.
    """
    appgini_messages = crud.crud_appgini_message.get_multi(db, skip=skip, limit=limit)
    return appgini_messages

@router.get("/{id}", response_model=schemas.AppginiMessage)
def read_appgini_message(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.AppginiMessage:
    """
    Get appgini_message by id.
    """
    db_appgini_message = crud.crud_appgini_message.get(db=db, id=id)
    if not db_appgini_message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="AppginiMessage not found")
    return db_appgini_message

@router.put("/{id}", response_model=schemas.AppginiMessage)
def update_appgini_message(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    appgini_message_in: schemas.AppginiMessageUpdate
) -> models.AppginiMessage:
    """
    Update appgini_message.
    """
    db_appgini_message = crud.crud_appgini_message.get(db=db, id=id)
    if not db_appgini_message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="AppginiMessage not found")
    appgini_message = crud.crud_appgini_message.update(db=db, db_obj=db_appgini_message, obj_in=appgini_message_in)
    return appgini_message

@router.delete("/{id}", response_model=schemas.AppginiMessage)
def delete_appgini_message(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.AppginiMessage:
    """
    Delete a appgini_message.
    """
    db_appgini_message = crud.crud_appgini_message.get(db=db, id=id)
    if not db_appgini_message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="AppginiMessage not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_appgini_message = crud.crud_appgini_message.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_appgini_message is None and db_appgini_message is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting AppginiMessage")
    return db_appgini_message # Return the object that was found by get, as per response_model
