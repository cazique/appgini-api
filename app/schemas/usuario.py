from datetime import date
from datetime import datetime
from pydantic import BaseModel
from typing import List
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .actividad import Actividad
    from .agencia import Agencia
    from .cliente import Cliente
    from .noticia import Noticia


from datetime import date
from datetime import datetime
from pydantic import BaseModel
from typing import List
from typing import Optional


class UsuarioBase(BaseModel):
    usuario_id: str
    nombre: str
    apellidos: str
    nombre_completo: Optional[str] = None
    email: Optional[str] = None
    telefono: Optional[str] = None
    puesto: Optional[str] = None
    agencia_id: Optional[str] = None
    activo: Optional[bool] = None
    fecha_alta: Optional[date] = None
    ultima_conexion: Optional[datetime] = None


class UsuarioCreate(UsuarioBase):
    nombre: str
    apellidos: str
    nombre_completo: Optional[str] = None
    email: Optional[str] = None
    telefono: Optional[str] = None
    puesto: Optional[str] = None
    agencia_id: Optional[str] = None
    activo: Optional[bool] = None
    fecha_alta: Optional[date] = None
    ultima_conexion: Optional[datetime] = None


class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    apellidos: Optional[str] = None
    nombre_completo: Optional[str] = None
    email: Optional[str] = None
    telefono: Optional[str] = None
    puesto: Optional[str] = None
    agencia_id: Optional[str] = None
    activo: Optional[bool] = None
    fecha_alta: Optional[date] = None
    ultima_conexion: Optional[datetime] = None


class Usuario(UsuarioBase):
    agencia: Optional['Agencia'] = None
    agencias_como_responsable: Optional[List['Agencia']] = None
    actividades: Optional[List['Actividad']] = None
    clientes: Optional[List['Cliente']] = None
    noticias_colaboradas: Optional[List['Noticia']] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
