from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.AppginiQueryLogEntry)
def create_appgini_query_log_entry(
    *,
    db: Session = Depends(deps.get_db),
    appgini_query_log_entry_in: schemas.AppginiQueryLogEntryCreate
) -> models.AppginiQueryLogEntry:
    """
    Create new appgini_query_log_entry.
    """
    appgini_query_log_entry = crud.crud_appgini_query_log_entry.create(db=db, obj_in=appgini_query_log_entry_in)
    return appgini_query_log_entry

@router.get("/", response_model=List[schemas.AppginiQueryLogEntry])
def read_appgini_query_log_entries(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve appgini_query_log_entries.
    """
    appgini_query_log_entries = crud.crud_appgini_query_log_entry.get_multi(db, skip=skip, limit=limit)
    return appgini_query_log_entries

@router.get("/{id}", response_model=schemas.AppginiQueryLogEntry)
def read_appgini_query_log_entry(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.AppginiQueryLogEntry:
    """
    Get appgini_query_log_entry by id.
    """
    db_appgini_query_log_entry = crud.crud_appgini_query_log_entry.get(db=db, id=id)
    if not db_appgini_query_log_entry:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="AppginiQueryLogEntry not found")
    return db_appgini_query_log_entry

@router.put("/{id}", response_model=schemas.AppginiQueryLogEntry)
def update_appgini_query_log_entry(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    appgini_query_log_entry_in: schemas.AppginiQueryLogEntryUpdate
) -> models.AppginiQueryLogEntry:
    """
    Update appgini_query_log_entry.
    """
    db_appgini_query_log_entry = crud.crud_appgini_query_log_entry.get(db=db, id=id)
    if not db_appgini_query_log_entry:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="AppginiQueryLogEntry not found")
    appgini_query_log_entry = crud.crud_appgini_query_log_entry.update(db=db, db_obj=db_appgini_query_log_entry, obj_in=appgini_query_log_entry_in)
    return appgini_query_log_entry

@router.delete("/{id}", response_model=schemas.AppginiQueryLogEntry)
def delete_appgini_query_log_entry(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.AppginiQueryLogEntry:
    """
    Delete a appgini_query_log_entry.
    """
    db_appgini_query_log_entry = crud.crud_appgini_query_log_entry.get(db=db, id=id)
    if not db_appgini_query_log_entry:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="AppginiQueryLogEntry not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_appgini_query_log_entry = crud.crud_appgini_query_log_entry.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_appgini_query_log_entry is None and db_appgini_query_log_entry is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting AppginiQueryLogEntry")
    return db_appgini_query_log_entry # Return the object that was found by get, as per response_model
