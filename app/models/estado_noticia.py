from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .noticia import Noticia

class EstadoNoticia(Base):
    __tablename__ = "estados_noticia"

    estado_noticia_id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), unique=True, nullable=False)
    descripcion = Column(String(200))
    orden = Column(Integer, default=0)
    color = Column(String(7), default='#000000')

    # Relationships
    noticias = relationship("Noticia", back_populates="estado_noticia")

    def __repr__(self):
        return f"<EstadoNoticia estado_noticia_id={getattr(self, 'estado_noticia_id', 'N/A')} nombre='{getattr(self, 'nombre', 'N/A')}'>"
