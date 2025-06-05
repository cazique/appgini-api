from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.MembershipUserrecord)
def create_membership_userrecord(
    *,
    db: Session = Depends(deps.get_db),
    membership_userrecord_in: schemas.MembershipUserrecordCreate
) -> models.MembershipUserrecord:
    """
    Create new membership_userrecord.
    """
    membership_userrecord = crud.crud_membership_userrecord.create(db=db, obj_in=membership_userrecord_in)
    return membership_userrecord

@router.get("/", response_model=List[schemas.MembershipUserrecord])
def read_membership_userrecords(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve membership_userrecords.
    """
    membership_userrecords = crud.crud_membership_userrecord.get_multi(db, skip=skip, limit=limit)
    return membership_userrecords

@router.get("/{id}", response_model=schemas.MembershipUserrecord)
def read_membership_userrecord(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.MembershipUserrecord:
    """
    Get membership_userrecord by id.
    """
    db_membership_userrecord = crud.crud_membership_userrecord.get(db=db, id=id)
    if not db_membership_userrecord:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MembershipUserrecord not found")
    return db_membership_userrecord

@router.put("/{id}", response_model=schemas.MembershipUserrecord)
def update_membership_userrecord(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    membership_userrecord_in: schemas.MembershipUserrecordUpdate
) -> models.MembershipUserrecord:
    """
    Update membership_userrecord.
    """
    db_membership_userrecord = crud.crud_membership_userrecord.get(db=db, id=id)
    if not db_membership_userrecord:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MembershipUserrecord not found")
    membership_userrecord = crud.crud_membership_userrecord.update(db=db, db_obj=db_membership_userrecord, obj_in=membership_userrecord_in)
    return membership_userrecord

@router.delete("/{id}", response_model=schemas.MembershipUserrecord)
def delete_membership_userrecord(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.MembershipUserrecord:
    """
    Delete a membership_userrecord.
    """
    db_membership_userrecord = crud.crud_membership_userrecord.get(db=db, id=id)
    if not db_membership_userrecord:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="MembershipUserrecord not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_membership_userrecord = crud.crud_membership_userrecord.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_membership_userrecord is None and db_membership_userrecord is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting MembershipUserrecord")
    return db_membership_userrecord # Return the object that was found by get, as per response_model
