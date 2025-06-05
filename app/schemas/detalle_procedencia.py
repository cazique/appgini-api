from pydantic import BaseModel
from typing import List
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .noticia import Noticia
    from .tipo_procedencia import TipoProcedencia


from pydantic import BaseModel
from typing import List
from typing import Optional


class DetalleProcedenciaBase(BaseModel):
    detalle_procedencia_id: int
    tipo_procedencia_id: int
    nombre: str
    descripcion: Optional[str] = None


class DetalleProcedenciaCreate(DetalleProcedenciaBase):
    tipo_procedencia_id: int
    nombre: str
    descripcion: Optional[str] = None


class DetalleProcedenciaUpdate(BaseModel):
    tipo_procedencia_id: Optional[int] = None
    nombre: Optional[str] = None
    descripcion: Optional[str] = None


class DetalleProcedencia(DetalleProcedenciaBase):
    tipo_procedencia: Optional['TipoProcedencia'] = None
    noticias: Optional[List['Noticia']] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
