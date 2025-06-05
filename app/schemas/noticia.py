from datetime import date
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .cliente import Cliente
    from .detalle_procedencia import DetalleProcedencia
    from .estado_contacto import EstadoContacto
    from .estado_noticia import EstadoNoticia
    from .inmueble import Inmueble
    from .motivo_cierre import MotivoCierre
    from .tipo_procedencia import TipoProcedencia
    from .usuario import Usuario


from datetime import date
from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel
from typing import Optional


class NoticiaBase(BaseModel):
    noticia_id: str
    referencia: Optional[str] = None
    inmueble_id: Optional[str] = None
    cliente_id: Optional[str] = None
    colaborador_id: Optional[str] = None
    estado_noticia_id: Optional[int] = None
    estado_contacto_id: Optional[int] = None
    tipo_procedencia_id: Optional[int] = None
    detalle_procedencia_id: Optional[int] = None
    motivacion: str
    valoracion: Optional[Decimal] = None
    valoracion_solo_inmueble: Optional[Decimal] = None
    precio_pedido: Optional[Decimal] = None
    fecha_valoracion: Optional[date] = None
    fecha_estimacion_interna: Optional[date] = None
    fecha_ultima_cita: Optional[date] = None
    fecha_ultimo_contacto: Optional[date] = None
    fecha_cierre: Optional[date] = None
    motivo_cierre_id: Optional[int] = None
    nota: Optional[str] = None
    fecha_creacion: Optional[datetime] = None
    fecha_modificacion: Optional[datetime] = None


class NoticiaCreate(NoticiaBase):
    referencia: Optional[str] = None
    inmueble_id: Optional[str] = None
    cliente_id: Optional[str] = None
    colaborador_id: Optional[str] = None
    estado_noticia_id: Optional[int] = None
    estado_contacto_id: Optional[int] = None
    tipo_procedencia_id: Optional[int] = None
    detalle_procedencia_id: Optional[int] = None
    motivacion: str
    valoracion: Optional[Decimal] = None
    valoracion_solo_inmueble: Optional[Decimal] = None
    precio_pedido: Optional[Decimal] = None
    fecha_valoracion: Optional[date] = None
    fecha_estimacion_interna: Optional[date] = None
    fecha_ultima_cita: Optional[date] = None
    fecha_ultimo_contacto: Optional[date] = None
    fecha_cierre: Optional[date] = None
    motivo_cierre_id: Optional[int] = None
    nota: Optional[str] = None
    fecha_creacion: Optional[datetime] = None
    fecha_modificacion: Optional[datetime] = None


class NoticiaUpdate(BaseModel):
    referencia: Optional[str] = None
    inmueble_id: Optional[str] = None
    cliente_id: Optional[str] = None
    colaborador_id: Optional[str] = None
    estado_noticia_id: Optional[int] = None
    estado_contacto_id: Optional[int] = None
    tipo_procedencia_id: Optional[int] = None
    detalle_procedencia_id: Optional[int] = None
    motivacion: Optional[str] = None
    valoracion: Optional[Decimal] = None
    valoracion_solo_inmueble: Optional[Decimal] = None
    precio_pedido: Optional[Decimal] = None
    fecha_valoracion: Optional[date] = None
    fecha_estimacion_interna: Optional[date] = None
    fecha_ultima_cita: Optional[date] = None
    fecha_ultimo_contacto: Optional[date] = None
    fecha_cierre: Optional[date] = None
    motivo_cierre_id: Optional[int] = None
    nota: Optional[str] = None
    fecha_creacion: Optional[datetime] = None
    fecha_modificacion: Optional[datetime] = None


class Noticia(NoticiaBase):
    inmueble: Optional['Inmueble'] = None
    cliente: Optional['Cliente'] = None
    colaborador: Optional['Usuario'] = None
    estado_noticia: Optional['EstadoNoticia'] = None
    estado_contacto: Optional['EstadoContacto'] = None
    tipo_procedencia: Optional['TipoProcedencia'] = None
    detalle_procedencia: Optional['DetalleProcedencia'] = None
    motivo_cierre: Optional['MotivoCierre'] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
