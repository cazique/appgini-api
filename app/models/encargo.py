from sqlalchemy import Column, Integer, String, Text, Date, DateTime, Boolean, Numeric, ForeignKey, func
from sqlalchemy.orm import relationship
from .database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .inmueble import Inmueble
    from .cliente import Cliente
    from .estado_encargo import EstadoEncargo
    from .estado_contacto import EstadoContacto
    from .tipo_procedencia import TipoProcedencia
    from .motivo_cierre import MotivoCierre
    from .actividad_encargo import ActividadEncargo

class Encargo(Base):
    __tablename__ = "encargos"

    encargo_id = Column(String(20), primary_key=True)
    referencia = Column(String(30))
    inmueble_id = Column(String(20), ForeignKey('inmuebles.inmueble_id'), nullable=False, index=True)
    propietario_id = Column(String(20), ForeignKey('clientes.cliente_id'), nullable=False, index=True)
    estado_id = Column(Integer, ForeignKey('estados_encargo.estado_id'), nullable=False, index=True)
    estado_contacto_id = Column(Integer, ForeignKey('estados_contacto.estado_contacto_id'))
    motivo = Column(String(40), nullable=False)
    tipo_procedencia_id = Column(Integer, ForeignKey('tipos_procedencia.tipo_procedencia_id'))
    precio = Column(Numeric(12, 2), nullable=False)
    precio_parking_incluido = Column(Boolean, default=False) # DDL default 0
    valoracion = Column(Numeric(12, 2))
    valoracion_solo_inmueble = Column(Numeric(12, 2))
    nuda_propiedad = Column(Boolean, default=False) # DDL default 0
    tratabilidad = Column(Integer) # DDL: TINYINT(4)
    fecha_creacion = Column(DateTime, server_default=func.now())
    fecha_modificacion = Column(DateTime, server_default=func.now(), onupdate=func.now())
    fecha_cierre = Column(Date)
    motivo_cierre_id = Column(Integer, ForeignKey('motivos_cierre.motivo_cierre_id'))
    fecha_ultima_cita = Column(Date)
    fecha_ultima_actividad = Column(Date)
    fecha_ultimo_contacto = Column(Date)
    nota_privada = Column(Text)
    llaves_oficina = Column(Boolean, default=False) # DDL default 0

    # Relationships
    inmueble = relationship("Inmueble", back_populates="encargos")
    propietario = relationship("Cliente", back_populates="encargos_como_propietario")
    estado = relationship("EstadoEncargo", back_populates="encargos")
    estado_contacto = relationship("EstadoContacto", back_populates="encargos")
    tipo_procedencia = relationship("TipoProcedencia", back_populates="encargos")
    motivo_cierre = relationship("MotivoCierre", back_populates="encargos")
    actividad_encargo_detalles = relationship("ActividadEncargo", back_populates="encargo")

    def __repr__(self):
        return f"<Encargo encargo_id='{getattr(self, 'encargo_id', 'N/A')}' referencia='{getattr(self, 'referencia', 'N/A')}'>"
