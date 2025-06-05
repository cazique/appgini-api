from datetime import date
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel
from typing import List
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .actividad_encargo import ActividadEncargo
    from .cliente import Cliente
    from .estado_contacto import EstadoContacto
    from .estado_encargo import EstadoEncargo
    from .inmueble import Inmueble
    from .motivo_cierre import MotivoCierre
    from .tipo_procedencia import TipoProcedencia


from datetime import date
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel
from typing import List
from typing import Optional


class EncargoBase(BaseModel):
    encargo_id: str
    referencia: Optional[str] = None
    inmueble_id: str
    propietario_id: str
    estado_id: int
    estado_contacto_id: Optional[int] = None
    motivo: str
    tipo_procedencia_id: Optional[int] = None
    precio: Decimal
    precio_parking_incluido: Optional[bool] = None
    valoracion: Optional[Decimal] = None
    valoracion_solo_inmueble: Optional[Decimal] = None
    nuda_propiedad: Optional[bool] = None
    tratabilidad: Optional[int] = None
    fecha_creacion: Optional[datetime] = None
    fecha_modificacion: Optional[datetime] = None
    fecha_cierre: Optional[date] = None
    motivo_cierre_id: Optional[int] = None
    fecha_ultima_cita: Optional[date] = None
    fecha_ultima_actividad: Optional[date] = None
    fecha_ultimo_contacto: Optional[date] = None
    nota_privada: Optional[str] = None
    llaves_oficina: Optional[bool] = None


class EncargoCreate(EncargoBase):
    referencia: Optional[str] = None
    inmueble_id: str
    propietario_id: str
    estado_id: int
    estado_contacto_id: Optional[int] = None
    motivo: str
    tipo_procedencia_id: Optional[int] = None
    precio: Decimal
    precio_parking_incluido: Optional[bool] = None
    valoracion: Optional[Decimal] = None
    valoracion_solo_inmueble: Optional[Decimal] = None
    nuda_propiedad: Optional[bool] = None
    tratabilidad: Optional[int] = None
    fecha_creacion: Optional[datetime] = None
    fecha_modificacion: Optional[datetime] = None
    fecha_cierre: Optional[date] = None
    motivo_cierre_id: Optional[int] = None
    fecha_ultima_cita: Optional[date] = None
    fecha_ultima_actividad: Optional[date] = None
    fecha_ultimo_contacto: Optional[date] = None
    nota_privada: Optional[str] = None
    llaves_oficina: Optional[bool] = None


class EncargoUpdate(BaseModel):
    referencia: Optional[str] = None
    inmueble_id: Optional[str] = None
    propietario_id: Optional[str] = None
    estado_id: Optional[int] = None
    estado_contacto_id: Optional[int] = None
    motivo: Optional[str] = None
    tipo_procedencia_id: Optional[int] = None
    precio: Optional[Decimal] = None
    precio_parking_incluido: Optional[bool] = None
    valoracion: Optional[Decimal] = None
    valoracion_solo_inmueble: Optional[Decimal] = None
    nuda_propiedad: Optional[bool] = None
    tratabilidad: Optional[int] = None
    fecha_creacion: Optional[datetime] = None
    fecha_modificacion: Optional[datetime] = None
    fecha_cierre: Optional[date] = None
    motivo_cierre_id: Optional[int] = None
    fecha_ultima_cita: Optional[date] = None
    fecha_ultima_actividad: Optional[date] = None
    fecha_ultimo_contacto: Optional[date] = None
    nota_privada: Optional[str] = None
    llaves_oficina: Optional[bool] = None


class Encargo(EncargoBase):
    inmueble: Optional['Inmueble'] = None
    propietario: Optional['Cliente'] = None
    estado: Optional['EstadoEncargo'] = None
    estado_contacto: Optional['EstadoContacto'] = None
    tipo_procedencia: Optional['TipoProcedencia'] = None
    motivo_cierre: Optional['MotivoCierre'] = None
    actividad_encargo_detalles: Optional[List['ActividadEncargo']] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
