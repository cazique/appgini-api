from pydantic import BaseModel
from typing import List
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .detalle_procedencia import DetalleProcedencia
    from .encargo import Encargo
    from .noticia import Noticia


from pydantic import BaseModel
from typing import List
from typing import Optional


class TipoProcedenciaBase(BaseModel):
    tipo_procedencia_id: int
    nombre: str
    descripcion: Optional[str] = None


class TipoProcedenciaCreate(TipoProcedenciaBase):
    nombre: str
    descripcion: Optional[str] = None


class TipoProcedenciaUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None


class TipoProcedencia(TipoProcedenciaBase):
    detalles_procedencia: Optional[List['DetalleProcedencia']] = None
    encargos: Optional[List['Encargo']] = None
    noticias: Optional[List['Noticia']] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
