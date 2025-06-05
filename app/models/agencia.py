from sqlalchemy import Column, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .usuario import Usuario
    from .cliente import Cliente

class Agencia(Base):
    __tablename__ = "agencias"

    agencia_id = Column(String(20), primary_key=True)
    nombre = Column(String(100), nullable=False)
    direccion = Column(String(200))
    codigo_postal = Column(String(10))
    localidad = Column(String(50))
    provincia = Column(String(50))
    telefono = Column(String(15))
    email = Column(String(100))
    responsable_id = Column(String(20), ForeignKey('usuarios.usuario_id'), index=True)
    fecha_alta = Column(Date)
    activo = Column(Boolean, default=True)

    # Relationships
    responsable = relationship("Usuario", foreign_keys=[responsable_id], back_populates="agencias_como_responsable")
    usuarios_en_agencia = relationship("Usuario", foreign_keys="[Usuario.agencia_id]", back_populates="agencia")
    clientes = relationship("Cliente", back_populates="agencia")

    def __repr__(self):
        return f"<Agencia agencia_id='{getattr(self, 'agencia_id', 'N/A')}' nombre='{getattr(self, 'nombre', 'N/A')}'>"
