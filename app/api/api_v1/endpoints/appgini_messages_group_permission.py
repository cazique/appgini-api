from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.AppginiMessagesGroupPermission)
def create_appgini_messages_group_permission(
    *,
    db: Session = Depends(deps.get_db),
    appgini_messages_group_permission_in: schemas.AppginiMessagesGroupPermissionCreate
) -> models.AppginiMessagesGroupPermission:
    """
    Create new appgini_messages_group_permission.
    """
    appgini_messages_group_permission = crud.crud_appgini_messages_group_permission.create(db=db, obj_in=appgini_messages_group_permission_in)
    return appgini_messages_group_permission

@router.get("/", response_model=List[schemas.AppginiMessagesGroupPermission])
def read_appgini_messages_group_permissions(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve appgini_messages_group_permissions.
    """
    appgini_messages_group_permissions = crud.crud_appgini_messages_group_permission.get_multi(db, skip=skip, limit=limit)
    return appgini_messages_group_permissions

@router.get("/{id}", response_model=schemas.AppginiMessagesGroupPermission)
def read_appgini_messages_group_permission(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.AppginiMessagesGroupPermission:
    """
    Get appgini_messages_group_permission by id.
    """
    db_appgini_messages_group_permission = crud.crud_appgini_messages_group_permission.get(db=db, id=id)
    if not db_appgini_messages_group_permission:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="AppginiMessagesGroupPermission not found")
    return db_appgini_messages_group_permission

@router.put("/{id}", response_model=schemas.AppginiMessagesGroupPermission)
def update_appgini_messages_group_permission(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    appgini_messages_group_permission_in: schemas.AppginiMessagesGroupPermissionUpdate
) -> models.AppginiMessagesGroupPermission:
    """
    Update appgini_messages_group_permission.
    """
    db_appgini_messages_group_permission = crud.crud_appgini_messages_group_permission.get(db=db, id=id)
    if not db_appgini_messages_group_permission:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="AppginiMessagesGroupPermission not found")
    appgini_messages_group_permission = crud.crud_appgini_messages_group_permission.update(db=db, db_obj=db_appgini_messages_group_permission, obj_in=appgini_messages_group_permission_in)
    return appgini_messages_group_permission

@router.delete("/{id}", response_model=schemas.AppginiMessagesGroupPermission)
def delete_appgini_messages_group_permission(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.AppginiMessagesGroupPermission:
    """
    Delete a appgini_messages_group_permission.
    """
    db_appgini_messages_group_permission = crud.crud_appgini_messages_group_permission.get(db=db, id=id)
    if not db_appgini_messages_group_permission:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="AppginiMessagesGroupPermission not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_appgini_messages_group_permission = crud.crud_appgini_messages_group_permission.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_appgini_messages_group_permission is None and db_appgini_messages_group_permission is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting AppginiMessagesGroupPermission")
    return db_appgini_messages_group_permission # Return the object that was found by get, as per response_model
