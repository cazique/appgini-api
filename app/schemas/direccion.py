from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .cliente import Cliente
    from .inmueble import Inmueble


from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel
from typing import Optional


class DireccionBase(BaseModel):
    direccion_id: int
    cliente_id: Optional[str] = None
    inmueble_id: Optional[str] = None
    tipo_direccion: str
    calle: str
    numero: Optional[str] = None
    piso: Optional[str] = None
    puerta: Optional[str] = None
    escalera: Optional[str] = None
    codigo_postal: Optional[str] = None
    localidad: str
    provincia: str
    pais: Optional[str] = None
    referencia_catastral: Optional[str] = None
    coordenadas_latitud: Optional[Decimal] = None
    coordenadas_longitud: Optional[Decimal] = None
    principal: Optional[bool] = None
    fecha_alta: Optional[datetime] = None
    ultima_modificacion: Optional[datetime] = None


class DireccionCreate(DireccionBase):
    cliente_id: Optional[str] = None
    inmueble_id: Optional[str] = None
    tipo_direccion: str
    calle: str
    numero: Optional[str] = None
    piso: Optional[str] = None
    puerta: Optional[str] = None
    escalera: Optional[str] = None
    codigo_postal: Optional[str] = None
    localidad: str
    provincia: str
    pais: Optional[str] = None
    referencia_catastral: Optional[str] = None
    coordenadas_latitud: Optional[Decimal] = None
    coordenadas_longitud: Optional[Decimal] = None
    principal: Optional[bool] = None
    fecha_alta: Optional[datetime] = None
    ultima_modificacion: Optional[datetime] = None


class DireccionUpdate(BaseModel):
    cliente_id: Optional[str] = None
    inmueble_id: Optional[str] = None
    tipo_direccion: Optional[str] = None
    calle: Optional[str] = None
    numero: Optional[str] = None
    piso: Optional[str] = None
    puerta: Optional[str] = None
    escalera: Optional[str] = None
    codigo_postal: Optional[str] = None
    localidad: Optional[str] = None
    provincia: Optional[str] = None
    pais: Optional[str] = None
    referencia_catastral: Optional[str] = None
    coordenadas_latitud: Optional[Decimal] = None
    coordenadas_longitud: Optional[Decimal] = None
    principal: Optional[bool] = None
    fecha_alta: Optional[datetime] = None
    ultima_modificacion: Optional[datetime] = None


class Direccion(DireccionBase):
    cliente: Optional['Cliente'] = None
    inmueble: Optional['Inmueble'] = None
    inmueble_primario_de: Optional['Inmueble'] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
