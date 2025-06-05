from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from .database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .encargo import Encargo
    from .noticia import Noticia

class MotivoCierre(Base):
    __tablename__ = "motivos_cierre"

    motivo_cierre_id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), unique=True, nullable=False)
    descripcion = Column(String(200))
    es_positivo = Column(Boolean, default=False)

    # Relationships
    encargos = relationship("Encargo", back_populates="motivo_cierre")
    noticias = relationship("Noticia", back_populates="motivo_cierre")

    def __repr__(self):
        return f"<MotivoCierre motivo_cierre_id={getattr(self, 'motivo_cierre_id', 'N/A')} nombre='{getattr(self, 'nombre', 'N/A')}'>"
