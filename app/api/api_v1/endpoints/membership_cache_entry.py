from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.MembershipCacheEntry)
def create_membership_cache_entry(
    *,
    db: Session = Depends(deps.get_db),
    membership_cache_entry_in: schemas.MembershipCacheEntryCreate
) -> models.MembershipCacheEntry:
    """
    Create new membership_cache_entry.
    """
    membership_cache_entry = crud.crud_membership_cache_entry.create(db=db, obj_in=membership_cache_entry_in)
    return membership_cache_entry

@router.get("/", response_model=List[schemas.MembershipCacheEntry])
def read_membership_cache_entries(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve membership_cache_entries.
    """
    membership_cache_entries = crud.crud_membership_cache_entry.get_multi(db, skip=skip, limit=limit)
    return membership_cache_entries

@router.get("/{id}", response_model=schemas.MembershipCacheEntry)
def read_membership_cache_entry(
    *,
    db: Session = Depends(deps.get_db),
    id: str
) -> models.MembershipCacheEntry:
    """
    Get membership_cache_entry by id.
    """
    db_membership_cache_entry = crud.crud_membership_cache_entry.get(db=db, id=id)
    if not db_membership_cache_entry:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MembershipCacheEntry not found")
    return db_membership_cache_entry

@router.put("/{id}", response_model=schemas.MembershipCacheEntry)
def update_membership_cache_entry(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    membership_cache_entry_in: schemas.MembershipCacheEntryUpdate
) -> models.MembershipCacheEntry:
    """
    Update membership_cache_entry.
    """
    db_membership_cache_entry = crud.crud_membership_cache_entry.get(db=db, id=id)
    if not db_membership_cache_entry:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MembershipCacheEntry not found")
    membership_cache_entry = crud.crud_membership_cache_entry.update(db=db, db_obj=db_membership_cache_entry, obj_in=membership_cache_entry_in)
    return membership_cache_entry

@router.delete("/{id}", response_model=schemas.MembershipCacheEntry)
def delete_membership_cache_entry(
    *,
    db: Session = Depends(deps.get_db),
    id: str
) -> models.MembershipCacheEntry:
    """
    Delete a membership_cache_entry.
    """
    db_membership_cache_entry = crud.crud_membership_cache_entry.get(db=db, id=id)
    if not db_membership_cache_entry:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MembershipCacheEntry not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_membership_cache_entry = crud.crud_membership_cache_entry.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_membership_cache_entry is None and db_membership_cache_entry is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting MembershipCacheEntry")
    return db_membership_cache_entry # Return the object that was found by get, as per response_model
