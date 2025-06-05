from sqlalchemy import Column, String, Date, Boolean, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from .database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .agencia import Agencia
    from .actividad import Actividad
    from .cliente import Cliente
    from .noticia import Noticia

class Usuario(Base):
    __tablename__ = "usuarios"

    usuario_id = Column(String(20), primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellidos = Column(String(100), nullable=False)
    nombre_completo = Column(String(150))
    email = Column(String(100), unique=True, index=True)
    telefono = Column(String(15))
    puesto = Column(String(50))
    agencia_id = Column(String(20), ForeignKey('agencias.agencia_id'), index=True)
    activo = Column(Boolean, default=True)
    fecha_alta = Column(Date, server_default=func.current_date())
    ultima_conexion = Column(DateTime)

    # Relationships
    agencia = relationship("Agencia", foreign_keys=[agencia_id], back_populates="usuarios_en_agencia")
    agencias_como_responsable = relationship("Agencia", foreign_keys="[Agencia.responsable_id]", back_populates="responsable")
    actividades = relationship("Actividad", back_populates="usuario")
    clientes = relationship("Cliente", back_populates="usuario")
    noticias_colaboradas = relationship("Noticia", back_populates="colaborador")

    # Consider link to MembershipUser if usuario_id can be memberID
    # membership_account = relationship("MembershipUser", primaryjoin="foreign(MembershipUser.memberID) == Usuario.usuario_id", back_populates="usuario_profile", uselist=False)

    def __repr__(self):
        return f"<Usuario usuario_id='{getattr(self, 'usuario_id', 'N/A')}' nombre_completo='{getattr(self, 'nombre_completo', 'N/A')}'>"
