from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .encargo import Encargo
    from .noticia import Noticia

class EstadoContacto(Base):
    __tablename__ = "estados_contacto"

    estado_contacto_id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), unique=True, nullable=False)
    descripcion = Column(String(200))
    dias_inactividad_min = Column(Integer, default=0)
    dias_inactividad_max = Column(Integer, default=999)
    orden = Column(Integer, default=0)
    color = Column(String(7), default='#000000')

    # Relationships
    encargos = relationship("Encargo", back_populates="estado_contacto")
    noticias = relationship("Noticia", back_populates="estado_contacto")

    def __repr__(self):
        return f"<EstadoContacto estado_contacto_id={getattr(self, 'estado_contacto_id', 'N/A')} nombre='{getattr(self, 'nombre', 'N/A')}'>"
