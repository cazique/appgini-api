from datetime import date
from pydantic import BaseModel
from typing import List
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .cliente import Cliente
    from .usuario import Usuario


from datetime import date
from pydantic import BaseModel
from typing import List
from typing import Optional


class AgenciaBase(BaseModel):
    agencia_id: str
    nombre: str
    direccion: Optional[str] = None
    codigo_postal: Optional[str] = None
    localidad: Optional[str] = None
    provincia: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None
    responsable_id: Optional[str] = None
    fecha_alta: Optional[date] = None
    activo: Optional[bool] = None


class AgenciaCreate(AgenciaBase):
    nombre: str
    direccion: Optional[str] = None
    codigo_postal: Optional[str] = None
    localidad: Optional[str] = None
    provincia: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None
    responsable_id: Optional[str] = None
    fecha_alta: Optional[date] = None
    activo: Optional[bool] = None


class AgenciaUpdate(BaseModel):
    nombre: Optional[str] = None
    direccion: Optional[str] = None
    codigo_postal: Optional[str] = None
    localidad: Optional[str] = None
    provincia: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None
    responsable_id: Optional[str] = None
    fecha_alta: Optional[date] = None
    activo: Optional[bool] = None


class Agencia(AgenciaBase):
    responsable: Optional['Usuario'] = None
    usuarios_en_agencia: Optional[List['Usuario']] = None
    clientes: Optional[List['Cliente']] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
