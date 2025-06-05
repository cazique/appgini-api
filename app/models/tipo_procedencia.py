from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .detalle_procedencia import DetalleProcedencia
    from .encargo import Encargo
    from .noticia import Noticia

class TipoProcedencia(Base):
    __tablename__ = "tipos_procedencia"

    tipo_procedencia_id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), unique=True, nullable=False)
    descripcion = Column(String(200))

    # Relationships
    detalles_procedencia = relationship("DetalleProcedencia", back_populates="tipo_procedencia", cascade="all, delete-orphan")
    encargos = relationship("Encargo", back_populates="tipo_procedencia")
    noticias = relationship("Noticia", back_populates="tipo_procedencia")

    def __repr__(self):
        return f"<TipoProcedencia tipo_procedencia_id={getattr(self, 'tipo_procedencia_id', 'N/A')} nombre='{getattr(self, 'nombre', 'N/A')}'>"
