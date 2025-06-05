from pydantic import BaseModel
from typing import List
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .inmueble import Inmueble
    from .subzona import Subzona


from pydantic import BaseModel
from typing import List
from typing import Optional


class ZonaBase(BaseModel):
    zona_id: int
    nombre: str
    localidad: str
    provincia: str
    descripcion: Optional[str] = None


class ZonaCreate(ZonaBase):
    nombre: str
    localidad: str
    provincia: str
    descripcion: Optional[str] = None


class ZonaUpdate(BaseModel):
    nombre: Optional[str] = None
    localidad: Optional[str] = None
    provincia: Optional[str] = None
    descripcion: Optional[str] = None


class Zona(ZonaBase):
    subzonas: Optional[List['Subzona']] = None
    inmuebles: Optional[List['Inmueble']] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
