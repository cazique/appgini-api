from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.MembershipGrouppermission)
def create_membership_grouppermission(
    *,
    db: Session = Depends(deps.get_db),
    membership_grouppermission_in: schemas.MembershipGrouppermissionCreate
) -> models.MembershipGrouppermission:
    """
    Create new membership_grouppermission.
    """
    membership_grouppermission = crud.crud_membership_grouppermission.create(db=db, obj_in=membership_grouppermission_in)
    return membership_grouppermission

@router.get("/", response_model=List[schemas.MembershipGrouppermission])
def read_membership_grouppermissions(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve membership_grouppermissions.
    """
    membership_grouppermissions = crud.crud_membership_grouppermission.get_multi(db, skip=skip, limit=limit)
    return membership_grouppermissions

@router.get("/{id}", response_model=schemas.MembershipGrouppermission)
def read_membership_grouppermission(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.MembershipGrouppermission:
    """
    Get membership_grouppermission by id.
    """
    db_membership_grouppermission = crud.crud_membership_grouppermission.get(db=db, id=id)
    if not db_membership_grouppermission:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MembershipGrouppermission not found")
    return db_membership_grouppermission

@router.put("/{id}", response_model=schemas.MembershipGrouppermission)
def update_membership_grouppermission(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    membership_grouppermission_in: schemas.MembershipGrouppermissionUpdate
) -> models.MembershipGrouppermission:
    """
    Update membership_grouppermission.
    """
    db_membership_grouppermission = crud.crud_membership_grouppermission.get(db=db, id=id)
    if not db_membership_grouppermission:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MembershipGrouppermission not found")
    membership_grouppermission = crud.crud_membership_grouppermission.update(db=db, db_obj=db_membership_grouppermission, obj_in=membership_grouppermission_in)
    return membership_grouppermission

@router.delete("/{id}", response_model=schemas.MembershipGrouppermission)
def delete_membership_grouppermission(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.MembershipGrouppermission:
    """
    Delete a membership_grouppermission.
    """
    db_membership_grouppermission = crud.crud_membership_grouppermission.get(db=db, id=id)
    if not db_membership_grouppermission:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MembershipGrouppermission not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_membership_grouppermission = crud.crud_membership_grouppermission.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_membership_grouppermission is None and db_membership_grouppermission is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting MembershipGrouppermission")
    return db_membership_grouppermission # Return the object that was found by get, as per response_model
