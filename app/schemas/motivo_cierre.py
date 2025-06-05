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


class MotivoCierreBase(BaseModel):
    motivo_cierre_id: int
    nombre: str
    descripcion: Optional[str] = None
    es_positivo: Optional[bool] = None


class MotivoCierreCreate(MotivoCierreBase):
    nombre: str
    descripcion: Optional[str] = None
    es_positivo: Optional[bool] = None


class MotivoCierreUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    es_positivo: Optional[bool] = None


class MotivoCierre(MotivoCierreBase):
    encargos: Optional[List['Encargo']] = None
    noticias: Optional[List['Noticia']] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
