from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .actividad import Actividad
    from .encargo import Encargo

class ActividadEncargo(Base):
    __tablename__ = "actividades_encargos"

    actividad_id = Column(String(20), ForeignKey('actividades.actividad_id'), primary_key=True)
    encargo_id = Column(String(20), ForeignKey('encargos.encargo_id'), nullable=False, index=True)

    # Relationships
    actividad = relationship("Actividad", back_populates="actividad_encargo_detalle")
    encargo = relationship("Encargo", back_populates="actividad_encargo_detalles")

    def __repr__(self):
        return f"<ActividadEncargo actividad_id='{getattr(self, 'actividad_id', 'N/A')}' encargo_id='{getattr(self, 'encargo_id', 'N/A')}'>"
