# This file makes Python treat the directory `models` as a package.

from .database import Base, engine, SessionLocal, get_db

# Import all refined model classes (singular filenames and class names)
from .actividad import Actividad
from .actividad_encargo import ActividadEncargo
from .agencia import Agencia
from .appgini_csv_import_job import AppginiCsvImportJob
from .appgini_message import AppginiMessage
from .appgini_messages_group_permission import AppginiMessagesGroupPermission
from .appgini_messages_setting import AppginiMessagesSetting
from .appgini_query_log_entry import AppginiQueryLogEntry
from .cliente import Cliente
from .detalle_procedencia import DetalleProcedencia
from .direccion import Direccion
from .encargo import Encargo
from .estado_contacto import EstadoContacto
from .estado_encargo import EstadoEncargo
from .estado_noticia import EstadoNoticia
from .inmueble import Inmueble
from .membership_cache_entry import MembershipCacheEntry
from .membership_grouppermission import MembershipGrouppermission
from .membership_group import MembershipGroup
from .membership_userpermission import MembershipUserpermission
from .membership_userrecord import MembershipUserrecord
from .membership_user import MembershipUser
from .membership_usersession import MembershipUsersession
from .modalidad_contacto import ModalidadContacto
from .motivo_cierre import MotivoCierre
from .noticia import Noticia
from .plantilla_pdf import PlantillaPdf
from .prioridad import Prioridad
from .subtipologia_inmueble import SubtipologiaInmueble
from .subzona import Subzona
from .tipologia_inmueble import TipologiaInmueble
from .tipo_actividad import TipoActividad
from .tipo_procedencia import TipoProcedencia
from .usuario import Usuario
from .zona import Zona

__all__ = [
    "Base", "engine", "SessionLocal", "get_db",
    "Actividad", "ActividadEncargo", "Agencia", "AppginiCsvImportJob",
    "AppginiMessage", "AppginiMessagesGroupPermission", "AppginiMessagesSetting",
    "AppginiQueryLogEntry", "Cliente", "DetalleProcedencia", "Direccion",
    "Encargo", "EstadoContacto", "EstadoEncargo", "EstadoNoticia", "Inmueble",
    "MembershipCacheEntry", "MembershipGrouppermission", "MembershipGroup",
    "MembershipUserpermission", "MembershipUserrecord", "MembershipUser",
    "MembershipUsersession", "ModalidadContacto", "MotivoCierre", "Noticia",
    "PlantillaPdf", "Prioridad", "SubtipologiaInmueble", "Subzona",
    "TipologiaInmueble", "TipoActividad", "TipoProcedencia", "Usuario", "Zona",
]
