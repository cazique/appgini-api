from sqlalchemy import Column, Integer, String, Text, Date, DateTime, Boolean, Numeric, ForeignKey, Time, func
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, Date, DateTime, Boolean, Numeric, ForeignKey, Time, func # Added all types used
from .database import Base
from typing import TYPE_CHECKING # Added TYPE_CHECKING

if TYPE_CHECKING:
    from .cliente import Cliente
    from .usuario import Usuario
    from .tipo_actividad import TipoActividad
    from .modalidad_contacto import ModalidadContacto
    from .prioridad import Prioridad
    from .actividad_encargo import ActividadEncargo
    # from .estados_actividad import EstadosActividad # If there's a status table

class Actividad(Base):
    __tablename__ = "actividades"

    actividad_id = Column(String(20), primary_key=True)
    referencia = Column(String(30))
    usuario_id = Column(String(20), ForeignKey('usuarios.usuario_id'), index=True)
    cliente_id = Column(String(20), ForeignKey('clientes.cliente_id'), index=True)
    asunto = Column(String(100), nullable=False)
    tipo_actividad_id = Column(Integer, ForeignKey('tipos_actividad.tipo_actividad_id'), index=True)
    modalidad_contacto_id = Column(Integer, ForeignKey('modalidades_contacto.modalidad_contacto_id'))
    fecha = Column(Date, nullable=False)
    hora_inicio = Column(Time)
    hora_fin = Column(Time)
    duracion_minutos = Column(Integer)
    prioridad_id = Column(Integer, ForeignKey('prioridades.prioridad_id'))
    estado_id = Column(Integer) # Placeholder: Link to a status table if applicable, e.g. ForeignKey('estados_actividad.id')
    descripcion = Column(Text)
    resultado = Column(Text)
    fecha_creacion = Column(DateTime, server_default=func.now())
    fecha_modificacion = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relationships
    cliente = relationship("Cliente", back_populates="actividades")
    usuario = relationship("Usuario", back_populates="actividades")
    tipo_actividad = relationship("TipoActividad", back_populates="actividades")
    modalidad_contacto = relationship("ModalidadContacto", back_populates="actividades")
    prioridad = relationship("Prioridad", back_populates="actividades")

    # Placeholder for estado relationship if 'estado_id' becomes a FK
    # estado = relationship("EstadosActividad")

    actividad_encargo_detalle = relationship("ActividadEncargo", uselist=False, back_populates="actividad")

    def __repr__(self):
        return f"<Actividad actividad_id={getattr(self, 'actividad_id', 'N/A')}>"
