from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.MembershipUser)
def create_membership_user(
    *,
    db: Session = Depends(deps.get_db),
    membership_user_in: schemas.MembershipUserCreate
) -> models.MembershipUser:
    """
    Create new membership_user.
    """
    membership_user = crud.crud_membership_user.create(db=db, obj_in=membership_user_in)
    return membership_user

@router.get("/", response_model=List[schemas.MembershipUser])
def read_membership_users(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve membership_users.
    """
    membership_users = crud.crud_membership_user.get_multi(db, skip=skip, limit=limit)
    return membership_users

@router.get("/{id}", response_model=schemas.MembershipUser)
def read_membership_user(
    *,
    db: Session = Depends(deps.get_db),
    id: str
) -> models.MembershipUser:
    """
    Get membership_user by id.
    """
    db_membership_user = crud.crud_membership_user.get(db=db, id=id)
    if not db_membership_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MembershipUser not found")
    return db_membership_user

@router.put("/{id}", response_model=schemas.MembershipUser)
def update_membership_user(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    membership_user_in: schemas.MembershipUserUpdate
) -> models.MembershipUser:
    """
    Update membership_user.
    """
    db_membership_user = crud.crud_membership_user.get(db=db, id=id)
    if not db_membership_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MembershipUser not found")
    membership_user = crud.crud_membership_user.update(db=db, db_obj=db_membership_user, obj_in=membership_user_in)
    return membership_user

@router.delete("/{id}", response_model=schemas.MembershipUser)
def delete_membership_user(
    *,
    db: Session = Depends(deps.get_db),
    id: str
) -> models.MembershipUser:
    """
    Delete a membership_user.
    """
    db_membership_user = crud.crud_membership_user.get(db=db, id=id)
    if not db_membership_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MembershipUser not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_membership_user = crud.crud_membership_user.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_membership_user is None and db_membership_user is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting MembershipUser")
    return db_membership_user # Return the object that was found by get, as per response_model
