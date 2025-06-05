from sqlalchemy import Column, Integer, String, Boolean, DateTime, Numeric, ForeignKey, func
from sqlalchemy.orm import relationship
from .database import Base
from .cliente import Cliente # Corrected: singular
from .inmueble import Inmueble # Corrected: singular

class Direccion(Base):
    __tablename__ = "direcciones"

    direccion_id = Column(Integer, primary_key=True, autoincrement=True)
    cliente_id = Column(String(20), ForeignKey('clientes.cliente_id'), index=True)
    inmueble_id = Column(String(20), ForeignKey('inmuebles.inmueble_id'), index=True)
    tipo_direccion = Column(String(40), nullable=False)
    calle = Column(String(100), nullable=False)
    numero = Column(String(10))
    piso = Column(String(10))
    puerta = Column(String(10))
    escalera = Column(String(10))
    codigo_postal = Column(String(10))
    localidad = Column(String(50), nullable=False)
    provincia = Column(String(50), nullable=False)
    pais = Column(String(50), default='Espana')
    referencia_catastral = Column(String(50))
    coordenadas_latitud = Column(Numeric(10, 8))
    coordenadas_longitud = Column(Numeric(11, 8))
    principal = Column(Boolean, default=False) # DDL default 0
    fecha_alta = Column(DateTime, server_default=func.now())
    ultima_modificacion = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relationships
    cliente = relationship("Cliente", back_populates="direcciones")
    # A Direccion can be linked to an Inmueble (e.g. an office address for an Inmueble that is a building)
    inmueble = relationship("Inmueble", foreign_keys=[inmueble_id], back_populates="todas_las_direcciones")
    # This Direccion might be the *primary* address for an Inmueble (linked via Inmueble.direccion_id)
    inmueble_primario_de = relationship("Inmueble", foreign_keys="[Inmueble.direccion_id]", back_populates="direccion", uselist=False)


    def __repr__(self):
        return f"<Direccion direccion_id={getattr(self, 'direccion_id', 'N/A')} calle='{getattr(self, 'calle', 'N/A')}'>"
