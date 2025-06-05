from datetime import date
from datetime import datetime
from datetime import time
from pydantic import BaseModel
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .actividad_encargo import ActividadEncargo
    from .cliente import Cliente
    from .modalidad_contacto import ModalidadContacto
    from .prioridad import Prioridad
    from .tipo_actividad import TipoActividad
    from .usuario import Usuario


from datetime import date
from datetime import datetime
from datetime import time
from pydantic import BaseModel
from typing import Optional


class ActividadBase(BaseModel):
    actividad_id: str
    referencia: Optional[str] = None
    usuario_id: Optional[str] = None
    cliente_id: Optional[str] = None
    asunto: str
    tipo_actividad_id: Optional[int] = None
    modalidad_contacto_id: Optional[int] = None
    fecha: date
    hora_inicio: Optional[time] = None
    hora_fin: Optional[time] = None
    duracion_minutos: Optional[int] = None
    prioridad_id: Optional[int] = None
    estado_id: Optional[int] = None
    descripcion: Optional[str] = None
    resultado: Optional[str] = None
    fecha_creacion: Optional[datetime] = None
    fecha_modificacion: Optional[datetime] = None


class ActividadCreate(ActividadBase):
    referencia: Optional[str] = None
    usuario_id: Optional[str] = None
    cliente_id: Optional[str] = None
    asunto: str
    tipo_actividad_id: Optional[int] = None
    modalidad_contacto_id: Optional[int] = None
    fecha: date
    hora_inicio: Optional[time] = None
    hora_fin: Optional[time] = None
    duracion_minutos: Optional[int] = None
    prioridad_id: Optional[int] = None
    estado_id: Optional[int] = None
    descripcion: Optional[str] = None
    resultado: Optional[str] = None
    fecha_creacion: Optional[datetime] = None
    fecha_modificacion: Optional[datetime] = None


class ActividadUpdate(BaseModel):
    referencia: Optional[str] = None
    usuario_id: Optional[str] = None
    cliente_id: Optional[str] = None
    asunto: Optional[str] = None
    tipo_actividad_id: Optional[int] = None
    modalidad_contacto_id: Optional[int] = None
    fecha: Optional[date] = None
    hora_inicio: Optional[time] = None
    hora_fin: Optional[time] = None
    duracion_minutos: Optional[int] = None
    prioridad_id: Optional[int] = None
    estado_id: Optional[int] = None
    descripcion: Optional[str] = None
    resultado: Optional[str] = None
    fecha_creacion: Optional[datetime] = None
    fecha_modificacion: Optional[datetime] = None


class Actividad(ActividadBase):
    cliente: Optional['Cliente'] = None
    usuario: Optional['Usuario'] = None
    tipo_actividad: Optional['TipoActividad'] = None
    modalidad_contacto: Optional['ModalidadContacto'] = None
    prioridad: Optional['Prioridad'] = None
    actividad_encargo_detalle: Optional['ActividadEncargo'] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
