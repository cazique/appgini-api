from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel
from typing import List
from typing import Optional
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .cliente import Cliente
    from .direccion import Direccion
    from .encargo import Encargo
    from .noticia import Noticia
    from .subtipologia_inmueble import SubtipologiaInmueble
    from .tipologia_inmueble import TipologiaInmueble
    from .zona import Zona


from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel
from typing import List
from typing import Optional


class InmuebleBase(BaseModel):
    inmueble_id: str
    referencia: Optional[str] = None
    propietario_id: Optional[str] = None
    estado: Optional[str] = None
    tipologia_id: Optional[int] = None
    subtipologia_id: Optional[int] = None
    direccion_id: Optional[int] = None
    zona_id: Optional[int] = None
    dormitorios: Optional[int] = None
    banos: Optional[int] = None
    aseos: Optional[int] = None
    m2_utiles: Optional[Decimal] = None
    m2_construidos: Optional[Decimal] = None
    m2_terraza: Optional[Decimal] = None
    altura: Optional[str] = None
    orientacion: Optional[str] = None
    estado_conservacion: Optional[str] = None
    ano_construccion: Optional[int] = None
    ano_reforma: Optional[int] = None
    ascensor: Optional[bool] = None
    terraza: Optional[bool] = None
    balcon: Optional[bool] = None
    garaje: Optional[bool] = None
    trastero: Optional[bool] = None
    calefaccion_tipo: Optional[str] = None
    climatizacion: Optional[str] = None
    certificado_energetico: Optional[str] = None
    consumo_energetico: Optional[Decimal] = None
    emisiones_co2: Optional[Decimal] = None
    referencia_catastral: Optional[str] = None
    fecha_alta: Optional[datetime] = None
    ultima_modificacion: Optional[datetime] = None
    llaves_oficina: Optional[bool] = None
    notas_privadas: Optional[str] = None
    observaciones: Optional[str] = None


class InmuebleCreate(InmuebleBase):
    referencia: Optional[str] = None
    propietario_id: Optional[str] = None
    estado: Optional[str] = None
    tipologia_id: Optional[int] = None
    subtipologia_id: Optional[int] = None
    direccion_id: Optional[int] = None
    zona_id: Optional[int] = None
    dormitorios: Optional[int] = None
    banos: Optional[int] = None
    aseos: Optional[int] = None
    m2_utiles: Optional[Decimal] = None
    m2_construidos: Optional[Decimal] = None
    m2_terraza: Optional[Decimal] = None
    altura: Optional[str] = None
    orientacion: Optional[str] = None
    estado_conservacion: Optional[str] = None
    ano_construccion: Optional[int] = None
    ano_reforma: Optional[int] = None
    ascensor: Optional[bool] = None
    terraza: Optional[bool] = None
    balcon: Optional[bool] = None
    garaje: Optional[bool] = None
    trastero: Optional[bool] = None
    calefaccion_tipo: Optional[str] = None
    climatizacion: Optional[str] = None
    certificado_energetico: Optional[str] = None
    consumo_energetico: Optional[Decimal] = None
    emisiones_co2: Optional[Decimal] = None
    referencia_catastral: Optional[str] = None
    fecha_alta: Optional[datetime] = None
    ultima_modificacion: Optional[datetime] = None
    llaves_oficina: Optional[bool] = None
    notas_privadas: Optional[str] = None
    observaciones: Optional[str] = None


class InmuebleUpdate(BaseModel):
    referencia: Optional[str] = None
    propietario_id: Optional[str] = None
    estado: Optional[str] = None
    tipologia_id: Optional[int] = None
    subtipologia_id: Optional[int] = None
    direccion_id: Optional[int] = None
    zona_id: Optional[int] = None
    dormitorios: Optional[int] = None
    banos: Optional[int] = None
    aseos: Optional[int] = None
    m2_utiles: Optional[Decimal] = None
    m2_construidos: Optional[Decimal] = None
    m2_terraza: Optional[Decimal] = None
    altura: Optional[str] = None
    orientacion: Optional[str] = None
    estado_conservacion: Optional[str] = None
    ano_construccion: Optional[int] = None
    ano_reforma: Optional[int] = None
    ascensor: Optional[bool] = None
    terraza: Optional[bool] = None
    balcon: Optional[bool] = None
    garaje: Optional[bool] = None
    trastero: Optional[bool] = None
    calefaccion_tipo: Optional[str] = None
    climatizacion: Optional[str] = None
    certificado_energetico: Optional[str] = None
    consumo_energetico: Optional[Decimal] = None
    emisiones_co2: Optional[Decimal] = None
    referencia_catastral: Optional[str] = None
    fecha_alta: Optional[datetime] = None
    ultima_modificacion: Optional[datetime] = None
    llaves_oficina: Optional[bool] = None
    notas_privadas: Optional[str] = None
    observaciones: Optional[str] = None


class Inmueble(InmuebleBase):
    propietario: Optional['Cliente'] = None
    tipologia: Optional['TipologiaInmueble'] = None
    subtipologia: Optional['SubtipologiaInmueble'] = None
    direccion: Optional['Direccion'] = None
    todas_las_direcciones: Optional[List['Direccion']] = None
    zona: Optional['Zona'] = None
    encargos: Optional[List['Encargo']] = None
    noticias: Optional[List['Noticia']] = None
    class Config:
        from_attributes = True  # Pydantic V2 setting
