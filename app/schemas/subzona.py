from pydantic import BaseModel
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .zona import Zona


from pydantic import BaseModel
from typing import Optional


class SubzonaBase(BaseModel):
    subzona_id: int
    zona_id: int
    nombre: str
    descripcion: Optional[str] = None


class SubzonaCreate(SubzonaBase):
    zona_id: int
    nombre: str
    descripcion: Optional[str] = None


class SubzonaUpdate(BaseModel):
    zona_id: Optional[int] = None
    nombre: Optional[str] = None
    descripcion: Optional[str] = None


class Subzona(SubzonaBase):
    zona: Optional['Zona'] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
