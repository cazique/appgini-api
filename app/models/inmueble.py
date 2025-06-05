from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, Numeric, ForeignKey, func
from sqlalchemy.orm import relationship
from .database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .cliente import Cliente
    from .tipologia_inmueble import TipologiaInmueble
    from .subtipologia_inmueble import SubtipologiaInmueble
    from .direccion import Direccion
    from .zona import Zona
    from .encargo import Encargo
    from .noticia import Noticia

class Inmueble(Base):
    __tablename__ = "inmuebles"

    inmueble_id = Column(String(20), primary_key=True)
    referencia = Column(String(30))
    propietario_id = Column(String(20), ForeignKey('clientes.cliente_id'), index=True)
    estado = Column(String(40), default='Disponible')
    tipologia_id = Column(Integer, ForeignKey('tipologias_inmueble.tipologia_id'), index=True)
    subtipologia_id = Column(Integer, ForeignKey('subtipologias_inmueble.subtipologia_id'))
    direccion_id = Column(Integer, ForeignKey('direcciones.direccion_id'), unique=True)
    zona_id = Column(Integer, ForeignKey('zonas.zona_id'))
    dormitorios = Column(Integer) # DDL: TINYINT(4)
    banos = Column(Integer) # DDL: TINYINT(4)
    aseos = Column(Integer) # DDL: TINYINT(4)
    m2_utiles = Column(Numeric(8, 2))
    m2_construidos = Column(Numeric(8, 2))
    m2_terraza = Column(Numeric(8, 2))
    altura = Column(String(20))
    orientacion = Column(String(30))
    estado_conservacion = Column(String(30))
    ano_construccion = Column(Integer) # DDL: SMALLINT(6)
    ano_reforma = Column(Integer) # DDL: SMALLINT(6)
    ascensor = Column(Boolean, default=False) # DDL default 0
    terraza = Column(Boolean, default=False) # DDL default 0
    balcon = Column(Boolean, default=False) # DDL default 0
    garaje = Column(Boolean, default=False) # DDL default 0
    trastero = Column(Boolean, default=False) # DDL default 0
    calefaccion_tipo = Column(String(50))
    climatizacion = Column(String(50))
    certificado_energetico = Column(String(5))
    consumo_energetico = Column(Numeric(8, 2))
    emisiones_co2 = Column(Numeric(8, 2))
    referencia_catastral = Column(String(50))
    fecha_alta = Column(DateTime, server_default=func.now())
    ultima_modificacion = Column(DateTime, server_default=func.now(), onupdate=func.now())
    llaves_oficina = Column(Boolean, default=False) # DDL default 0
    notas_privadas = Column(Text)
    observaciones = Column(Text)

    # Relationships
    propietario = relationship("Cliente", back_populates="inmuebles_como_propietario")
    tipologia = relationship("TipologiaInmueble", back_populates="inmuebles")
    subtipologia = relationship("SubtipologiaInmueble", back_populates="inmuebles")

    direccion = relationship("Direccion", foreign_keys=[direccion_id], back_populates="inmueble_primario_de", uselist=False)
    todas_las_direcciones = relationship("Direccion", foreign_keys="[Direccion.inmueble_id]", back_populates="inmueble", cascade="all, delete-orphan")

    zona = relationship("Zona", back_populates="inmuebles")
    encargos = relationship("Encargo", back_populates="inmueble", cascade="all, delete-orphan")
    noticias = relationship("Noticia", back_populates="inmueble", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Inmueble inmueble_id='{getattr(self, 'inmueble_id', 'N/A')}' referencia='{getattr(self, 'referencia', 'N/A')}'>"
