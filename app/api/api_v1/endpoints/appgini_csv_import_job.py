from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.AppginiCsvImportJob)
def create_appgini_csv_import_job(
    *,
    db: Session = Depends(deps.get_db),
    appgini_csv_import_job_in: schemas.AppginiCsvImportJobCreate
) -> models.AppginiCsvImportJob:
    """
    Create new appgini_csv_import_job.
    """
    appgini_csv_import_job = crud.crud_appgini_csv_import_job.create(db=db, obj_in=appgini_csv_import_job_in)
    return appgini_csv_import_job

@router.get("/", response_model=List[schemas.AppginiCsvImportJob])
def read_appgini_csv_import_jobs(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve appgini_csv_import_jobs.
    """
    appgini_csv_import_jobs = crud.crud_appgini_csv_import_job.get_multi(db, skip=skip, limit=limit)
    return appgini_csv_import_jobs

@router.get("/{id}", response_model=schemas.AppginiCsvImportJob)
def read_appgini_csv_import_job(
    *,
    db: Session = Depends(deps.get_db),
    id: str
) -> models.AppginiCsvImportJob:
    """
    Get appgini_csv_import_job by id.
    """
    db_appgini_csv_import_job = crud.crud_appgini_csv_import_job.get(db=db, id=id)
    if not db_appgini_csv_import_job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="AppginiCsvImportJob not found")
    return db_appgini_csv_import_job

@router.put("/{id}", response_model=schemas.AppginiCsvImportJob)
def update_appgini_csv_import_job(
    *,
    db: Session = Depends(deps.get_db),
    id: str,
    appgini_csv_import_job_in: schemas.AppginiCsvImportJobUpdate
) -> models.AppginiCsvImportJob:
    """
    Update appgini_csv_import_job.
    """
    db_appgini_csv_import_job = crud.crud_appgini_csv_import_job.get(db=db, id=id)
    if not db_appgini_csv_import_job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="AppginiCsvImportJob not found")
    appgini_csv_import_job = crud.crud_appgini_csv_import_job.update(db=db, db_obj=db_appgini_csv_import_job, obj_in=appgini_csv_import_job_in)
    return appgini_csv_import_job

@router.delete("/{id}", response_model=schemas.AppginiCsvImportJob)
def delete_appgini_csv_import_job(
    *,
    db: Session = Depends(deps.get_db),
    id: str
) -> models.AppginiCsvImportJob:
    """
    Delete a appgini_csv_import_job.
    """
    db_appgini_csv_import_job = crud.crud_appgini_csv_import_job.get(db=db, id=id)
    if not db_appgini_csv_import_job:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="AppginiCsvImportJob not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_appgini_csv_import_job = crud.crud_appgini_csv_import_job.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_appgini_csv_import_job is None and db_appgini_csv_import_job is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting AppginiCsvImportJob")
    return db_appgini_csv_import_job # Return the object that was found by get, as per response_model
