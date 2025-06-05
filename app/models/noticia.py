from sqlalchemy import Column, Integer, String, Text, Date, DateTime, Numeric, ForeignKey, func
from sqlalchemy.orm import relationship
from .database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .inmueble import Inmueble
    from .cliente import Cliente
    from .usuario import Usuario
    from .estado_noticia import EstadoNoticia
    from .estado_contacto import EstadoContacto
    from .tipo_procedencia import TipoProcedencia
    from .detalle_procedencia import DetalleProcedencia
    from .motivo_cierre import MotivoCierre

class Noticia(Base):
    __tablename__ = "noticias"

    noticia_id = Column(String(20), primary_key=True)
    referencia = Column(String(30))
    inmueble_id = Column(String(20), ForeignKey('inmuebles.inmueble_id'), index=True)
    cliente_id = Column(String(20), ForeignKey('clientes.cliente_id'), index=True)
    colaborador_id = Column(String(20), ForeignKey('usuarios.usuario_id'), index=True)
    estado_noticia_id = Column(Integer, ForeignKey('estados_noticia.estado_noticia_id'), index=True)
    estado_contacto_id = Column(Integer, ForeignKey('estados_contacto.estado_contacto_id'))
    tipo_procedencia_id = Column(Integer, ForeignKey('tipos_procedencia.tipo_procedencia_id'))
    detalle_procedencia_id = Column(Integer, ForeignKey('detalles_procedencia.detalle_procedencia_id'))
    motivacion = Column(String(40), nullable=False)
    valoracion = Column(Numeric(12, 2))
    valoracion_solo_inmueble = Column(Numeric(12, 2))
    precio_pedido = Column(Numeric(12, 2))
    fecha_valoracion = Column(Date)
    fecha_estimacion_interna = Column(Date)
    fecha_ultima_cita = Column(Date)
    fecha_ultimo_contacto = Column(Date)
    fecha_cierre = Column(Date)
    motivo_cierre_id = Column(Integer, ForeignKey('motivos_cierre.motivo_cierre_id'))
    nota = Column(Text)
    fecha_creacion = Column(DateTime, server_default=func.now())
    fecha_modificacion = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relationships
    inmueble = relationship("Inmueble", back_populates="noticias")
    cliente = relationship("Cliente", back_populates="noticias")
    colaborador = relationship("Usuario", back_populates="noticias_colaboradas")
    estado_noticia = relationship("EstadoNoticia", back_populates="noticias")
    estado_contacto = relationship("EstadoContacto", back_populates="noticias")
    tipo_procedencia = relationship("TipoProcedencia", back_populates="noticias")
    detalle_procedencia = relationship("DetalleProcedencia", back_populates="noticias")
    motivo_cierre = relationship("MotivoCierre", back_populates="noticias")

    def __repr__(self):
        return f"<Noticia noticia_id='{getattr(self, 'noticia_id', 'N/A')}' referencia='{getattr(self, 'referencia', 'N/A')}'>"
