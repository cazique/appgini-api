from datetime import datetime
from pydantic import BaseModel
from typing import Optional


from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class PlantillaPdfBase(BaseModel):
    zona_id: int
    nombre: Optional[str] = None
    tabla: Optional[str] = None
    html: Optional[str] = None
    grupo_autorizado: Optional[str] = None
    usuario_id: Optional[str] = None
    fecha_creacion: Optional[datetime] = None
    fecha_modificacion: Optional[datetime] = None
    nota: Optional[str] = None


class PlantillaPdfCreate(PlantillaPdfBase):
    nombre: Optional[str] = None
    tabla: Optional[str] = None
    html: Optional[str] = None
    grupo_autorizado: Optional[str] = None
    usuario_id: Optional[str] = None
    fecha_creacion: Optional[datetime] = None
    fecha_modificacion: Optional[datetime] = None
    nota: Optional[str] = None


class PlantillaPdfUpdate(BaseModel):
    nombre: Optional[str] = None
    tabla: Optional[str] = None
    html: Optional[str] = None
    grupo_autorizado: Optional[str] = None
    usuario_id: Optional[str] = None
    fecha_creacion: Optional[datetime] = None
    fecha_modificacion: Optional[datetime] = None
    nota: Optional[str] = None


class PlantillaPdf(PlantillaPdfBase):
    class Config:
        from_attributes = True  # Pydantic V2 setting
