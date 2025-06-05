from datetime import date
from datetime import datetime
from pydantic import BaseModel
from typing import List
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .actividad import Actividad
    from .agencia import Agencia
    from .direccion import Direccion
    from .encargo import Encargo
    from .inmueble import Inmueble
    from .noticia import Noticia
    from .usuario import Usuario


from datetime import date
from datetime import datetime
from pydantic import BaseModel
from typing import List
from typing import Optional


class ClienteBase(BaseModel):
    cliente_id: str
    nombre: str
    apellidos: str
    nombre_completo: Optional[str] = None
    tratamiento: Optional[str] = None
    genero: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    documento_id: Optional[str] = None
    nacionalidad: Optional[str] = None
    estado_civil: Optional[str] = None
    telefono_fijo: Optional[str] = None
    telefono_movil: Optional[str] = None
    telefono_adicional: Optional[str] = None
    email: Optional[str] = None
    cliente_telefonico: Optional[bool] = None
    profesion: Optional[str] = None
    sector_actividad: Optional[str] = None
    empresa: Optional[str] = None
    fecha_alta: Optional[date] = None
    ultima_modificacion: Optional[datetime] = None
    agencia_id: Optional[str] = None
    usuario_id: Optional[str] = None
    observaciones: Optional[str] = None


class ClienteCreate(ClienteBase):
    nombre: str
    apellidos: str
    nombre_completo: Optional[str] = None
    tratamiento: Optional[str] = None
    genero: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    documento_id: Optional[str] = None
    nacionalidad: Optional[str] = None
    estado_civil: Optional[str] = None
    telefono_fijo: Optional[str] = None
    telefono_movil: Optional[str] = None
    telefono_adicional: Optional[str] = None
    email: Optional[str] = None
    cliente_telefonico: Optional[bool] = None
    profesion: Optional[str] = None
    sector_actividad: Optional[str] = None
    empresa: Optional[str] = None
    fecha_alta: Optional[date] = None
    ultima_modificacion: Optional[datetime] = None
    agencia_id: Optional[str] = None
    usuario_id: Optional[str] = None
    observaciones: Optional[str] = None


class ClienteUpdate(BaseModel):
    nombre: Optional[str] = None
    apellidos: Optional[str] = None
    nombre_completo: Optional[str] = None
    tratamiento: Optional[str] = None
    genero: Optional[str] = None
    fecha_nacimiento: Optional[date] = None
    documento_id: Optional[str] = None
    nacionalidad: Optional[str] = None
    estado_civil: Optional[str] = None
    telefono_fijo: Optional[str] = None
    telefono_movil: Optional[str] = None
    telefono_adicional: Optional[str] = None
    email: Optional[str] = None
    cliente_telefonico: Optional[bool] = None
    profesion: Optional[str] = None
    sector_actividad: Optional[str] = None
    empresa: Optional[str] = None
    fecha_alta: Optional[date] = None
    ultima_modificacion: Optional[datetime] = None
    agencia_id: Optional[str] = None
    usuario_id: Optional[str] = None
    observaciones: Optional[str] = None


class Cliente(ClienteBase):
    agencia: Optional['Agencia'] = None
    usuario: Optional['Usuario'] = None
    actividades: Optional[List['Actividad']] = None
    direcciones: Optional[List['Direccion']] = None
    encargos_como_propietario: Optional[List['Encargo']] = None
    inmuebles_como_propietario: Optional[List['Inmueble']] = None
    noticias: Optional[List['Noticia']] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
