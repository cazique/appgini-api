from pydantic import BaseModel
from typing import List
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .encargo import Encargo


from pydantic import BaseModel
from typing import List
from typing import Optional


class EstadoEncargoBase(BaseModel):
    estado_id: int
    nombre: str
    descripcion: Optional[str] = None
    orden: Optional[int] = None
    color: Optional[str] = None


class EstadoEncargoCreate(EstadoEncargoBase):
    nombre: str
    descripcion: Optional[str] = None
    orden: Optional[int] = None
    color: Optional[str] = None


class EstadoEncargoUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    orden: Optional[int] = None
    color: Optional[str] = None


class EstadoEncargo(EstadoEncargoBase):
    encargos: Optional[List['Encargo']] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
