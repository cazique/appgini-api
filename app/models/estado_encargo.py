from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .encargo import Encargo

class EstadoEncargo(Base):
    __tablename__ = "estados_encargo"

    estado_id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), unique=True, nullable=False)
    descripcion = Column(String(200))
    orden = Column(Integer, default=0)
    color = Column(String(7), default='#000000')

    # Relationships
    encargos = relationship("Encargo", back_populates="estado")

    def __repr__(self):
        return f"<EstadoEncargo estado_id={getattr(self, 'estado_id', 'N/A')} nombre='{getattr(self, 'nombre', 'N/A')}'>"
