from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.MembershipUserpermission)
def create_membership_userpermission(
    *,
    db: Session = Depends(deps.get_db),
    membership_userpermission_in: schemas.MembershipUserpermissionCreate
) -> models.MembershipUserpermission:
    """
    Create new membership_userpermission.
    """
    membership_userpermission = crud.crud_membership_userpermission.create(db=db, obj_in=membership_userpermission_in)
    return membership_userpermission

@router.get("/", response_model=List[schemas.MembershipUserpermission])
def read_membership_userpermissions(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve membership_userpermissions.
    """
    membership_userpermissions = crud.crud_membership_userpermission.get_multi(db, skip=skip, limit=limit)
    return membership_userpermissions

@router.get("/{id}", response_model=schemas.MembershipUserpermission)
def read_membership_userpermission(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.MembershipUserpermission:
    """
    Get membership_userpermission by id.
    """
    db_membership_userpermission = crud.crud_membership_userpermission.get(db=db, id=id)
    if not db_membership_userpermission:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MembershipUserpermission not found")
    return db_membership_userpermission

@router.put("/{id}", response_model=schemas.MembershipUserpermission)
def update_membership_userpermission(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    membership_userpermission_in: schemas.MembershipUserpermissionUpdate
) -> models.MembershipUserpermission:
    """
    Update membership_userpermission.
    """
    db_membership_userpermission = crud.crud_membership_userpermission.get(db=db, id=id)
    if not db_membership_userpermission:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MembershipUserpermission not found")
    membership_userpermission = crud.crud_membership_userpermission.update(db=db, db_obj=db_membership_userpermission, obj_in=membership_userpermission_in)
    return membership_userpermission

@router.delete("/{id}", response_model=schemas.MembershipUserpermission)
def delete_membership_userpermission(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.MembershipUserpermission:
    """
    Delete a membership_userpermission.
    """
    db_membership_userpermission = crud.crud_membership_userpermission.get(db=db, id=id)
    if not db_membership_userpermission:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MembershipUserpermission not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_membership_userpermission = crud.crud_membership_userpermission.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_membership_userpermission is None and db_membership_userpermission is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting MembershipUserpermission")
    return db_membership_userpermission # Return the object that was found by get, as per response_model
