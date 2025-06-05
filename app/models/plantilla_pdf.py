from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from .database import Base
# from .usuarios import Usuario # If usuario_id is a FK to usuarios.usuario_id
# from .membership_groups import MembershipGroup # If grupo_autorizado is a FK

class PlantillaPdf(Base):
    __tablename__ = "plantillas_pdf"

    # DDL PK is zona_id, which is unusual for a table named plantillas_pdf.
    # Assuming 'zona_id' is a typo in the DDL's PK for this table and should be e.g. 'plantilla_id' or similar.
    # For now, using 'plantilla_pdf_id' as the PK for clarity and ORM compatibility.
    # If 'zona_id' truly is the PK and relates to 'zonas' table, this needs to be adjusted.
    # The DDL shows `zona_id int(11) NOT NULL AUTO_INCREMENT` as PK. Will stick to DDL name for PK.
    zona_id = Column(Integer, primary_key=True, autoincrement=True)

    nombre = Column(String(255))
    tabla = Column(String(255)) # Table this template applies to
    html = Column(String(255)) # Path to HTML template or content
    grupo_autorizado = Column(String(255)) # Potential FK to membership_groups.name or groupID
    usuario_id = Column(String(255)) # Potential FK to usuarios.usuario_id or membership_users.memberID
    fecha_creacion = Column(DateTime, server_default=func.now())
    fecha_modificacion = Column(DateTime, server_default=func.now(), onupdate=func.now())
    nota = Column(Text)

    # Potential relationships (commented out due to ambiguity of FK targets)
    # If grupo_autorizado refers to membership_groups.groupID (assuming it's an INT after conversion):
    # authorized_group = relationship("MembershipGroup", foreign_keys="[cast(PlantillaPdf.grupo_autorizado, Integer)]", primaryjoin="cast(PlantillaPdf.grupo_autorizado, Integer) == MembershipGroup.groupID")
    # If usuario_id refers to usuarios.usuario_id:
    # creator_user = relationship("Usuario", foreign_keys=[usuario_id], primaryjoin="PlantillaPdf.usuario_id == Usuario.usuario_id")

    def __repr__(self):
        return f"<PlantillaPdf zona_id={getattr(self, 'zona_id', 'N/A')} nombre='{getattr(self, 'nombre', 'N/A')}'>"
