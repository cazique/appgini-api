from pydantic import BaseModel
from typing import List
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .actividad import Actividad


from pydantic import BaseModel
from typing import List
from typing import Optional


class PrioridadBase(BaseModel):
    prioridad_id: int
    nombre: str
    descripcion: Optional[str] = None
    orden: Optional[int] = None
    color: Optional[str] = None


class PrioridadCreate(PrioridadBase):
    nombre: str
    descripcion: Optional[str] = None
    orden: Optional[int] = None
    color: Optional[str] = None


class PrioridadUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    orden: Optional[int] = None
    color: Optional[str] = None


class Prioridad(PrioridadBase):
    actividades: Optional[List['Actividad']] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
