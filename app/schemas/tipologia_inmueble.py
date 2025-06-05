from pydantic import BaseModel
from typing import List
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .inmueble import Inmueble
    from .subtipologia_inmueble import SubtipologiaInmueble


from pydantic import BaseModel
from typing import List
from typing import Optional


class TipologiaInmuebleBase(BaseModel):
    tipologia_id: int
    nombre: str
    descripcion: Optional[str] = None


class TipologiaInmuebleCreate(TipologiaInmuebleBase):
    nombre: str
    descripcion: Optional[str] = None


class TipologiaInmuebleUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None


class TipologiaInmueble(TipologiaInmuebleBase):
    subtipologias: Optional[List['SubtipologiaInmueble']] = None
    inmuebles: Optional[List['Inmueble']] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
