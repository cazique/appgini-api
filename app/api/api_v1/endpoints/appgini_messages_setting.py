from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.AppginiMessagesSetting)
def create_appgini_messages_setting(
    *,
    db: Session = Depends(deps.get_db),
    appgini_messages_setting_in: schemas.AppginiMessagesSettingCreate
) -> models.AppginiMessagesSetting:
    """
    Create new appgini_messages_setting.
    """
    appgini_messages_setting = crud.crud_appgini_messages_setting.create(db=db, obj_in=appgini_messages_setting_in)
    return appgini_messages_setting

@router.get("/", response_model=List[schemas.AppginiMessagesSetting])
def read_appgini_messages_settings(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve appgini_messages_settings.
    """
    appgini_messages_settings = crud.crud_appgini_messages_setting.get_multi(db, skip=skip, limit=limit)
    return appgini_messages_settings

@router.get("/{id}", response_model=schemas.AppginiMessagesSetting)
def read_appgini_messages_setting(
    *,
    db: Session = Depends(deps.get_db),
    id: str
) -> models.AppginiMessagesSetting:
    """
    Get appgini_messages_setting by id.
    """
    db_appgini_messages_setting = crud.crud_appgini_messages_setting.get(db=db, id=id)
    if not db_appgini_messages_setting:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="AppginiMessagesSetting not found")
    return db_appgini_messages_setting

@router.put("/{id}", response_model=schemas.AppginiMessagesSetting)
def update_appgini_messages_setting(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    appgini_messages_setting_in: schemas.AppginiMessagesSettingUpdate
) -> models.AppginiMessagesSetting:
    """
    Update appgini_messages_setting.
    """
    db_appgini_messages_setting = crud.crud_appgini_messages_setting.get(db=db, id=id)
    if not db_appgini_messages_setting:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="AppginiMessagesSetting not found")
    appgini_messages_setting = crud.crud_appgini_messages_setting.update(db=db, db_obj=db_appgini_messages_setting, obj_in=appgini_messages_setting_in)
    return appgini_messages_setting

@router.delete("/{id}", response_model=schemas.AppginiMessagesSetting)
def delete_appgini_messages_setting(
    *,
    db: Session = Depends(deps.get_db),
    id: str
) -> models.AppginiMessagesSetting:
    """
    Delete a appgini_messages_setting.
    """
    db_appgini_messages_setting = crud.crud_appgini_messages_setting.get(db=db, id=id)
    if not db_appgini_messages_setting:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="AppginiMessagesSetting not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_appgini_messages_setting = crud.crud_appgini_messages_setting.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_appgini_messages_setting is None and db_appgini_messages_setting is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting AppginiMessagesSetting")
    return db_appgini_messages_setting # Return the object that was found by get, as per response_model
