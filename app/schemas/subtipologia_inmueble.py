from pydantic import BaseModel
from typing import List
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .inmueble import Inmueble
    from .tipologia_inmueble import TipologiaInmueble


from pydantic import BaseModel
from typing import List
from typing import Optional


class SubtipologiaInmuebleBase(BaseModel):
    subtipologia_id: int
    tipologia_id: int
    nombre: str
    descripcion: Optional[str] = None


class SubtipologiaInmuebleCreate(SubtipologiaInmuebleBase):
    tipologia_id: int
    nombre: str
    descripcion: Optional[str] = None


class SubtipologiaInmuebleUpdate(BaseModel):
    tipologia_id: Optional[int] = None
    nombre: Optional[str] = None
    descripcion: Optional[str] = None


class SubtipologiaInmueble(SubtipologiaInmuebleBase):
    tipologia: Optional['TipologiaInmueble'] = None
    inmuebles: Optional[List['Inmueble']] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
