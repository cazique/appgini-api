from pydantic import BaseModel
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .actividad import Actividad
    from .encargo import Encargo


from pydantic import BaseModel
from typing import Optional


class ActividadEncargoBase(BaseModel):
    actividad_id: str
    encargo_id: str


class ActividadEncargoCreate(ActividadEncargoBase):
    encargo_id: str


class ActividadEncargoUpdate(BaseModel):
    encargo_id: Optional[str] = None


class ActividadEncargo(ActividadEncargoBase):
    actividad: Optional['Actividad'] = None
    encargo: Optional['Encargo'] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
