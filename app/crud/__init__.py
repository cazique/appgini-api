# This file makes Python treat the directory `crud` as a package.

# Import all CRUD modules for easier access from services or routers
from . import crud_plantilla_pdf
from . import crud_membership_grouppermission
from . import crud_appgini_messages_setting
from . import crud_inmueble
from . import crud_appgini_csv_import_job
from . import crud_actividad_encargo
from . import crud_appgini_message
from . import crud_subtipologia_inmueble
from . import crud_membership_userpermission
from . import crud_actividad
from . import crud_appgini_messages_group_permission
from . import crud_usuario
from . import crud_tipo_procedencia
from . import crud_encargo
from . import crud_membership_group
from . import crud_estado_contacto
from . import crud_membership_userrecord
from . import crud_estado_encargo
from . import crud_membership_user
from . import crud_agencia
from . import crud_appgini_query_log_entry
from . import crud_tipologia_inmueble
from . import crud_tipo_actividad
from . import crud_direccion
from . import crud_membership_usersession
from . import crud_prioridad
from . import crud_membership_cache_entry
from . import crud_cliente
from . import crud_estado_noticia
from . import crud_modalidad_contacto
from . import crud_subzona
from . import crud_detalle_procedencia
from . import crud_motivo_cierre
from . import crud_noticia
from . import crud_zona


__all__ = [
    "crud_plantilla_pdf",
    "crud_membership_grouppermission",
    "crud_appgini_messages_setting",
    "crud_inmueble",
    "crud_appgini_csv_import_job",
    "crud_actividad_encargo",
    "crud_appgini_message",
    "crud_subtipologia_inmueble",
    "crud_membership_userpermission",
    "crud_actividad",
    "crud_appgini_messages_group_permission",
    "crud_usuario",
    "crud_tipo_procedencia",
    "crud_encargo",
    "crud_membership_group",
    "crud_estado_contacto",
    "crud_membership_userrecord",
    "crud_estado_encargo",
    "crud_membership_user",
    "crud_agencia",
    "crud_appgini_query_log_entry",
    "crud_tipologia_inmueble",
    "crud_tipo_actividad",
    "crud_direccion",
    "crud_membership_usersession",
    "crud_prioridad",
    "crud_membership_cache_entry",
    "crud_cliente",
    "crud_estado_noticia",
    "crud_modalidad_contacto",
    "crud_subzona",
    "crud_detalle_procedencia",
    "crud_motivo_cierre",
    "crud_noticia",
    "crud_zona",
]
