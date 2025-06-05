from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.MembershipUsersession)
def create_membership_usersession(
    *,
    db: Session = Depends(deps.get_db),
    membership_usersession_in: schemas.MembershipUsersessionCreate
) -> models.MembershipUsersession:
    """
    Create new membership_usersession.
    """
    membership_usersession = crud.crud_membership_usersession.create(db=db, obj_in=membership_usersession_in)
    return membership_usersession

@router.get("/", response_model=List[schemas.MembershipUsersession])
def read_membership_usersessions(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve membership_usersessions.
    """
    membership_usersessions = crud.crud_membership_usersession.get_multi(db, skip=skip, limit=limit)
    return membership_usersessions

@router.get("/{id}", response_model=schemas.MembershipUsersession)
def read_membership_usersession(
    *,
    db: Session = Depends(deps.get_db),
    id: str
) -> models.MembershipUsersession:
    """
    Get membership_usersession by id.
    """
    db_membership_usersession = crud.crud_membership_usersession.get(db=db, id=id)
    if not db_membership_usersession:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MembershipUsersession not found")
    return db_membership_usersession

@router.put("/{id}", response_model=schemas.MembershipUsersession)
def update_membership_usersession(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    membership_usersession_in: schemas.MembershipUsersessionUpdate
) -> models.MembershipUsersession:
    """
    Update membership_usersession.
    """
    db_membership_usersession = crud.crud_membership_usersession.get(db=db, id=id)
    if not db_membership_usersession:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MembershipUsersession not found")
    membership_usersession = crud.crud_membership_usersession.update(db=db, db_obj=db_membership_usersession, obj_in=membership_usersession_in)
    return membership_usersession

@router.delete("/{id}", response_model=schemas.MembershipUsersession)
def delete_membership_usersession(
    *,
    db: Session = Depends(deps.get_db),
    id: str
) -> models.MembershipUsersession:
    """
    Delete a membership_usersession.
    """
    db_membership_usersession = crud.crud_membership_usersession.get(db=db, id=id)
    if not db_membership_usersession:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MembershipUsersession not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_membership_usersession = crud.crud_membership_usersession.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_membership_usersession is None and db_membership_usersession is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting MembershipUsersession")
    return db_membership_usersession # Return the object that was found by get, as per response_model
