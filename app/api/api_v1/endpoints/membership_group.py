from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.MembershipGroup)
def create_membership_group(
    *,
    db: Session = Depends(deps.get_db),
    membership_group_in: schemas.MembershipGroupCreate
) -> models.MembershipGroup:
    """
    Create new membership_group.
    """
    membership_group = crud.crud_membership_group.create(db=db, obj_in=membership_group_in)
    return membership_group

@router.get("/", response_model=List[schemas.MembershipGroup])
def read_membership_groups(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve membership_groups.
    """
    membership_groups = crud.crud_membership_group.get_multi(db, skip=skip, limit=limit)
    return membership_groups

@router.get("/{id}", response_model=schemas.MembershipGroup)
def read_membership_group(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.MembershipGroup:
    """
    Get membership_group by id.
    """
    db_membership_group = crud.crud_membership_group.get(db=db, id=id)
    if not db_membership_group:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MembershipGroup not found")
    return db_membership_group

@router.put("/{id}", response_model=schemas.MembershipGroup)
def update_membership_group(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    membership_group_in: schemas.MembershipGroupUpdate
) -> models.MembershipGroup:
    """
    Update membership_group.
    """
    db_membership_group = crud.crud_membership_group.get(db=db, id=id)
    if not db_membership_group:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MembershipGroup not found")
    membership_group = crud.crud_membership_group.update(db=db, db_obj=db_membership_group, obj_in=membership_group_in)
    return membership_group

@router.delete("/{id}", response_model=schemas.MembershipGroup)
def delete_membership_group(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.MembershipGroup:
    """
    Delete a membership_group.
    """
    db_membership_group = crud.crud_membership_group.get(db=db, id=id)
    if not db_membership_group:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MembershipGroup not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_membership_group = crud.crud_membership_group.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_membership_group is None and db_membership_group is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting MembershipGroup")
    return db_membership_group # Return the object that was found by get, as per response_model
