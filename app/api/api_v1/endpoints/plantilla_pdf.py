from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, models, schemas # General imports
from app.api import deps # For get_db dependency

router = APIRouter()

@router.post("/", response_model=schemas.PlantillaPdf)
def create_plantilla_pdf(
    *,
    db: Session = Depends(deps.get_db),
    plantilla_pdf_in: schemas.PlantillaPdfCreate
) -> models.PlantillaPdf:
    """
    Create new plantilla_pdf.
    """
    plantilla_pdf = crud.crud_plantilla_pdf.create(db=db, obj_in=plantilla_pdf_in)
    return plantilla_pdf

@router.get("/", response_model=List[schemas.PlantillaPdf])
def read_plantilla_pdfs(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve plantilla_pdfs.
    """
    plantilla_pdfs = crud.crud_plantilla_pdf.get_multi(db, skip=skip, limit=limit)
    return plantilla_pdfs

@router.get("/{id}", response_model=schemas.PlantillaPdf)
def read_plantilla_pdf(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.PlantillaPdf:
    """
    Get plantilla_pdf by id.
    """
    db_plantilla_pdf = crud.crud_plantilla_pdf.get(db=db, id=id)
    if not db_plantilla_pdf:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="PlantillaPdf not found")
    return db_plantilla_pdf

@router.put("/{id}", response_model=schemas.PlantillaPdf)
def update_plantilla_pdf(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    plantilla_pdf_in: schemas.PlantillaPdfUpdate
) -> models.PlantillaPdf:
    """
    Update plantilla_pdf.
    """
    db_plantilla_pdf = crud.crud_plantilla_pdf.get(db=db, id=id)
    if not db_plantilla_pdf:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="PlantillaPdf not found")
    plantilla_pdf = crud.crud_plantilla_pdf.update(db=db, db_obj=db_plantilla_pdf, obj_in=plantilla_pdf_in)
    return plantilla_pdf

@router.delete("/{id}", response_model=schemas.PlantillaPdf)
def delete_plantilla_pdf(
    *,
    db: Session = Depends(deps.get_db),
    id: int
) -> models.PlantillaPdf:
    """
    Delete a plantilla_pdf.
    """
    db_plantilla_pdf = crud.crud_plantilla_pdf.get(db=db, id=id)
    if not db_plantilla_pdf:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="PlantillaPdf not found")
    # Ensure the crud remove function can handle the actual db_obj or its id
    # Current crud.remove takes id. If it returned the object, this is fine.
    deleted_plantilla_pdf = crud.crud_plantilla_pdf.remove(db=db, id=id)
    # If remove returns None when not found (though we check above), or the object upon success:
    if deleted_plantilla_pdf is None and db_plantilla_pdf is not None:
        # This case implies .remove() failed internally after .get() found it. Unlikely with current crud.remove.
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Error deleting PlantillaPdf")
    return db_plantilla_pdf # Return the object that was found by get, as per response_model
