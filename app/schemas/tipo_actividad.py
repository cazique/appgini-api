from pydantic import BaseModel
from typing import List
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .actividad import Actividad


from pydantic import BaseModel
from typing import List
from typing import Optional


class TipoActividadBase(BaseModel):
    tipo_actividad_id: int
    nombre: str
    descripcion: Optional[str] = None
    requiere_resultado: Optional[bool] = None


class TipoActividadCreate(TipoActividadBase):
    nombre: str
    descripcion: Optional[str] = None
    requiere_resultado: Optional[bool] = None


class TipoActividadUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    requiere_resultado: Optional[bool] = None


class TipoActividad(TipoActividadBase):
    actividades: Optional[List['Actividad']] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
