from sqlalchemy import Column, String, Date, Boolean, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from .database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .agencia import Agencia
    from .usuario import Usuario
    from .actividad import Actividad
    from .direccion import Direccion
    from .encargo import Encargo
    from .inmueble import Inmueble
    from .noticia import Noticia

class Cliente(Base):
    __tablename__ = "clientes"

    cliente_id = Column(String(20), primary_key=True)
    nombre = Column(String(50), nullable=False)
    apellidos = Column(String(100), nullable=False)
    nombre_completo = Column(String(150))
    tratamiento = Column(String(10))
    genero = Column(String(40))
    fecha_nacimiento = Column(Date)
    documento_id = Column(String(20), unique=True)
    nacionalidad = Column(String(50))
    estado_civil = Column(String(30))
    telefono_fijo = Column(String(15))
    telefono_movil = Column(String(15))
    telefono_adicional = Column(String(15))
    email = Column(String(100))
    cliente_telefonico = Column(Boolean, default=False) # DDL default 0
    profesion = Column(String(100))
    sector_actividad = Column(String(100))
    empresa = Column(String(100))
    fecha_alta = Column(Date)
    ultima_modificacion = Column(DateTime, server_default=func.now(), onupdate=func.now())
    agencia_id = Column(String(20), ForeignKey('agencias.agencia_id'), index=True)
    usuario_id = Column(String(20), ForeignKey('usuarios.usuario_id'), index=True) # User who manages this client
    observaciones = Column(Text)

    # Relationships
    agencia = relationship("Agencia", back_populates="clientes")
    usuario = relationship("Usuario", back_populates="clientes")

    actividades = relationship("Actividad", back_populates="cliente", cascade="all, delete-orphan")
    direcciones = relationship("Direccion", back_populates="cliente", cascade="all, delete-orphan")

    encargos_como_propietario = relationship("Encargo", foreign_keys="[Encargo.propietario_id]", back_populates="propietario", cascade="all, delete-orphan")
    inmuebles_como_propietario = relationship("Inmueble", foreign_keys="[Inmueble.propietario_id]", back_populates="propietario", cascade="all, delete-orphan")
    noticias = relationship("Noticia", back_populates="cliente", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Cliente cliente_id='{getattr(self, 'cliente_id', 'N/A')}' nombre_completo='{getattr(self, 'nombre_completo', 'N/A')}'>"
