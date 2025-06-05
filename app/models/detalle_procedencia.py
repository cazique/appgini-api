from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .tipo_procedencia import TipoProcedencia
    from .noticia import Noticia

class DetalleProcedencia(Base):
    __tablename__ = "detalles_procedencia"

    detalle_procedencia_id = Column(Integer, primary_key=True, autoincrement=True)
    tipo_procedencia_id = Column(Integer, ForeignKey('tipos_procedencia.tipo_procedencia_id'), nullable=False, index=True)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(String(200))

    # Relationships
    tipo_procedencia = relationship("TipoProcedencia", back_populates="detalles_procedencia")
    noticias = relationship("Noticia", back_populates="detalle_procedencia")

    def __repr__(self):
        return f"<DetalleProcedencia detalle_procedencia_id={getattr(self, 'detalle_procedencia_id', 'N/A')} nombre='{getattr(self, 'nombre', 'N/A')}'>"
