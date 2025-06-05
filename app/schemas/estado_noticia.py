from pydantic import BaseModel
from typing import List
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .noticia import Noticia


from pydantic import BaseModel
from typing import List
from typing import Optional


class EstadoNoticiaBase(BaseModel):
    estado_noticia_id: int
    nombre: str
    descripcion: Optional[str] = None
    orden: Optional[int] = None
    color: Optional[str] = None


class EstadoNoticiaCreate(EstadoNoticiaBase):
    nombre: str
    descripcion: Optional[str] = None
    orden: Optional[int] = None
    color: Optional[str] = None


class EstadoNoticiaUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    orden: Optional[int] = None
    color: Optional[str] = None


class EstadoNoticia(EstadoNoticiaBase):
    noticias: Optional[List['Noticia']] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
