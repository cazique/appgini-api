from pydantic import BaseModel
from typing import List
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .encargo import Encargo
    from .noticia import Noticia


from pydantic import BaseModel
from typing import List
from typing import Optional


class EstadoContactoBase(BaseModel):
    estado_contacto_id: int
    nombre: str
    descripcion: Optional[str] = None
    dias_inactividad_min: Optional[int] = None
    dias_inactividad_max: Optional[int] = None
    orden: Optional[int] = None
    color: Optional[str] = None


class EstadoContactoCreate(EstadoContactoBase):
    nombre: str
    descripcion: Optional[str] = None
    dias_inactividad_min: Optional[int] = None
    dias_inactividad_max: Optional[int] = None
    orden: Optional[int] = None
    color: Optional[str] = None


class EstadoContactoUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    dias_inactividad_min: Optional[int] = None
    dias_inactividad_max: Optional[int] = None
    orden: Optional[int] = None
    color: Optional[str] = None


class EstadoContacto(EstadoContactoBase):
    encargos: Optional[List['Encargo']] = None
    noticias: Optional[List['Noticia']] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
