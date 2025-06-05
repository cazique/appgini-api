from typing import Any, Dict, Optional, Union, List

from sqlalchemy.orm import Session

from app.models.appgini_query_log_entry import AppginiQueryLogEntry # Use model_name_str for consistency
from app.schemas.appgini_query_log_entry import AppginiQueryLogEntryCreate, AppginiQueryLogEntryUpdate

# Note: get_multi might need more sophisticated filtering/ordering in a real app

def get(db: Session, id: int) -> Optional[AppginiQueryLogEntry]:
    return db.query(AppginiQueryLogEntry).filter(AppginiQueryLogEntry.id == id).first()

def get_multi(db: Session, *, skip: int = 0, limit: int = 100) -> List[AppginiQueryLogEntry]:
    return db.query(AppginiQueryLogEntry).offset(skip).limit(limit).all()

def create(db: Session, *, obj_in: AppginiQueryLogEntryCreate) -> AppginiQueryLogEntry:
    db_obj = AppginiQueryLogEntry(**obj_in.model_dump())  # Pydantic v2
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update(
    db: Session,
    *,
    db_obj: AppginiQueryLogEntry,
    obj_in: Union[AppginiQueryLogEntryUpdate, Dict[str, Any]]
) -> AppginiQueryLogEntry:
    if isinstance(obj_in, dict):
        update_data = obj_in
    else:
        update_data = obj_in.model_dump(exclude_unset=True) # Pydantic v2

    # Ensure db_obj is not None before proceeding
    if db_obj is None:
        return None # Or raise HTTPException(status_code=404, detail="Object not found")

    for field, value in update_data.items():
        setattr(db_obj, field, value)

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def remove(db: Session, *, id: int) -> Optional[AppginiQueryLogEntry]:
    # For getattr, pk_name needs to be a string.
    # getattr(model_name, pk_column.name if pk_column else 'id') would try to get attribute from the class name string.
    # It should be getattr(globals()[model_name], pk_column.name if pk_column else 'id') or pass model_class
    # The current context is an f-string being written to a file, so AppginiQueryLogEntry is correct there.
    # The filter line inside the generated file should be:
    # obj = db.query(ModelName).filter(getattr(ModelName, "pk_attr_name") == id).first()
    # However, .get(id) is simpler if the PK type hint matches the actual PK type and it's a single PK.
    # The DDL parsing for PKs currently assumes 'id' or the first found PK.
    # If pk_name_for_template defaults to "id", this will use ModelName.id
    obj = db.query(AppginiQueryLogEntry).filter(AppginiQueryLogEntry.id == id).first()
    # A more robust get for single PKs would be:
    # obj = db.get(AppginiQueryLogEntry, id) # if pk_type_hint is guaranteed to match actual PK type
    # However, the filter approach is more general.
    if obj:
        db.delete(obj)
        db.commit()
    return obj
