from pydantic import BaseModel
from typing import List
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .actividad import Actividad


from pydantic import BaseModel
from typing import List
from typing import Optional


class ModalidadContactoBase(BaseModel):
    modalidad_contacto_id: int
    nombre: str
    descripcion: Optional[str] = None


class ModalidadContactoCreate(ModalidadContactoBase):
    nombre: str
    descripcion: Optional[str] = None


class ModalidadContactoUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None


class ModalidadContacto(ModalidadContactoBase):
    actividades: Optional[List['Actividad']] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
