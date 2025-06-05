from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .actividad import Actividad

class ModalidadContacto(Base):
    __tablename__ = "modalidades_contacto"

    modalidad_contacto_id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50), unique=True, nullable=False)
    descripcion = Column(String(200))

    # Relationships
    actividades = relationship("Actividad", back_populates="modalidad_contacto")

    def __repr__(self):
        return f"<ModalidadContacto modalidad_contacto_id={getattr(self, 'modalidad_contacto_id', 'N/A')} nombre='{getattr(self, 'nombre', 'N/A')}'>"
