# This file makes Python treat the directory `schemas` as a package.

# Import all Pydantic schemas for easier access
from .plantilla_pdf import PlantillaPdfBase, PlantillaPdfCreate, PlantillaPdfUpdate, PlantillaPdf
from .membership_grouppermission import MembershipGrouppermissionBase, MembershipGrouppermissionCreate, MembershipGrouppermissionUpdate, MembershipGrouppermission
from .appgini_messages_setting import AppginiMessagesSettingBase, AppginiMessagesSettingCreate, AppginiMessagesSettingUpdate, AppginiMessagesSetting
from .inmueble import InmuebleBase, InmuebleCreate, InmuebleUpdate, Inmueble
from .appgini_csv_import_job import AppginiCsvImportJobBase, AppginiCsvImportJobCreate, AppginiCsvImportJobUpdate, AppginiCsvImportJob
from .actividad_encargo import ActividadEncargoBase, ActividadEncargoCreate, ActividadEncargoUpdate, ActividadEncargo
from .appgini_message import AppginiMessageBase, AppginiMessageCreate, AppginiMessageUpdate, AppginiMessage
from .subtipologia_inmueble import SubtipologiaInmuebleBase, SubtipologiaInmuebleCreate, SubtipologiaInmuebleUpdate, SubtipologiaInmueble
from .membership_userpermission import MembershipUserpermissionBase, MembershipUserpermissionCreate, MembershipUserpermissionUpdate, MembershipUserpermission
from .actividad import ActividadBase, ActividadCreate, ActividadUpdate, Actividad
from .appgini_messages_group_permission import AppginiMessagesGroupPermissionBase, AppginiMessagesGroupPermissionCreate, AppginiMessagesGroupPermissionUpdate, AppginiMessagesGroupPermission
from .usuario import UsuarioBase, UsuarioCreate, UsuarioUpdate, Usuario
from .tipo_procedencia import TipoProcedenciaBase, TipoProcedenciaCreate, TipoProcedenciaUpdate, TipoProcedencia
from .encargo import EncargoBase, EncargoCreate, EncargoUpdate, Encargo
from .membership_group import MembershipGroupBase, MembershipGroupCreate, MembershipGroupUpdate, MembershipGroup
from .estado_contacto import EstadoContactoBase, EstadoContactoCreate, EstadoContactoUpdate, EstadoContacto
from .membership_userrecord import MembershipUserrecordBase, MembershipUserrecordCreate, MembershipUserrecordUpdate, MembershipUserrecord
from .estado_encargo import EstadoEncargoBase, EstadoEncargoCreate, EstadoEncargoUpdate, EstadoEncargo
from .membership_user import MembershipUserBase, MembershipUserCreate, MembershipUserUpdate, MembershipUser
from .agencia import AgenciaBase, AgenciaCreate, AgenciaUpdate, Agencia
from .appgini_query_log_entry import AppginiQueryLogEntryBase, AppginiQueryLogEntryCreate, AppginiQueryLogEntryUpdate, AppginiQueryLogEntry
from .tipologia_inmueble import TipologiaInmuebleBase, TipologiaInmuebleCreate, TipologiaInmuebleUpdate, TipologiaInmueble
from .tipo_actividad import TipoActividadBase, TipoActividadCreate, TipoActividadUpdate, TipoActividad
from .direccion import DireccionBase, DireccionCreate, DireccionUpdate, Direccion
from .membership_usersession import MembershipUsersessionBase, MembershipUsersessionCreate, MembershipUsersessionUpdate, MembershipUsersession
from .prioridad import PrioridadBase, PrioridadCreate, PrioridadUpdate, Prioridad
from .membership_cache_entry import MembershipCacheEntryBase, MembershipCacheEntryCreate, MembershipCacheEntryUpdate, MembershipCacheEntry
from .cliente import ClienteBase, ClienteCreate, ClienteUpdate, Cliente
from .estado_noticia import EstadoNoticiaBase, EstadoNoticiaCreate, EstadoNoticiaUpdate, EstadoNoticia
from .modalidad_contacto import ModalidadContactoBase, ModalidadContactoCreate, ModalidadContactoUpdate, ModalidadContacto
from .subzona import SubzonaBase, SubzonaCreate, SubzonaUpdate, Subzona
from .detalle_procedencia import DetalleProcedenciaBase, DetalleProcedenciaCreate, DetalleProcedenciaUpdate, DetalleProcedencia
from .motivo_cierre import MotivoCierreBase, MotivoCierreCreate, MotivoCierreUpdate, MotivoCierre
from .noticia import NoticiaBase, NoticiaCreate, NoticiaUpdate, Noticia
from .zona import ZonaBase, ZonaCreate, ZonaUpdate, Zona


__all__ = [
    "PlantillaPdfBase",
    "PlantillaPdfCreate",
    "PlantillaPdfUpdate",
    "PlantillaPdf",
    "MembershipGrouppermissionBase",
    "MembershipGrouppermissionCreate",
    "MembershipGrouppermissionUpdate",
    "MembershipGrouppermission",
    "AppginiMessagesSettingBase",
    "AppginiMessagesSettingCreate",
    "AppginiMessagesSettingUpdate",
    "AppginiMessagesSetting",
    "InmuebleBase",
    "InmuebleCreate",
    "InmuebleUpdate",
    "Inmueble",
    "AppginiCsvImportJobBase",
    "AppginiCsvImportJobCreate",
    "AppginiCsvImportJobUpdate",
    "AppginiCsvImportJob",
    "ActividadEncargoBase",
    "ActividadEncargoCreate",
    "ActividadEncargoUpdate",
    "ActividadEncargo",
    "AppginiMessageBase",
    "AppginiMessageCreate",
    "AppginiMessageUpdate",
    "AppginiMessage",
    "SubtipologiaInmuebleBase",
    "SubtipologiaInmuebleCreate",
    "SubtipologiaInmuebleUpdate",
    "SubtipologiaInmueble",
    "MembershipUserpermissionBase",
    "MembershipUserpermissionCreate",
    "MembershipUserpermissionUpdate",
    "MembershipUserpermission",
    "ActividadBase",
    "ActividadCreate",
    "ActividadUpdate",
    "Actividad",
    "AppginiMessagesGroupPermissionBase",
    "AppginiMessagesGroupPermissionCreate",
    "AppginiMessagesGroupPermissionUpdate",
    "AppginiMessagesGroupPermission",
    "UsuarioBase",
    "UsuarioCreate",
    "UsuarioUpdate",
    "Usuario",
    "TipoProcedenciaBase",
    "TipoProcedenciaCreate",
    "TipoProcedenciaUpdate",
    "TipoProcedencia",
    "EncargoBase",
    "EncargoCreate",
    "EncargoUpdate",
    "Encargo",
    "MembershipGroupBase",
    "MembershipGroupCreate",
    "MembershipGroupUpdate",
    "MembershipGroup",
    "EstadoContactoBase",
    "EstadoContactoCreate",
    "EstadoContactoUpdate",
    "EstadoContacto",
    "MembershipUserrecordBase",
    "MembershipUserrecordCreate",
    "MembershipUserrecordUpdate",
    "MembershipUserrecord",
    "EstadoEncargoBase",
    "EstadoEncargoCreate",
    "EstadoEncargoUpdate",
    "EstadoEncargo",
    "MembershipUserBase",
    "MembershipUserCreate",
    "MembershipUserUpdate",
    "MembershipUser",
    "AgenciaBase",
    "AgenciaCreate",
    "AgenciaUpdate",
    "Agencia",
    "AppginiQueryLogEntryBase",
    "AppginiQueryLogEntryCreate",
    "AppginiQueryLogEntryUpdate",
    "AppginiQueryLogEntry",
    "TipologiaInmuebleBase",
    "TipologiaInmuebleCreate",
    "TipologiaInmuebleUpdate",
    "TipologiaInmueble",
    "TipoActividadBase",
    "TipoActividadCreate",
    "TipoActividadUpdate",
    "TipoActividad",
    "DireccionBase",
    "DireccionCreate",
    "DireccionUpdate",
    "Direccion",
    "MembershipUsersessionBase",
    "MembershipUsersessionCreate",
    "MembershipUsersessionUpdate",
    "MembershipUsersession",
    "PrioridadBase",
    "PrioridadCreate",
    "PrioridadUpdate",
    "Prioridad",
    "MembershipCacheEntryBase",
    "MembershipCacheEntryCreate",
    "MembershipCacheEntryUpdate",
    "MembershipCacheEntry",
    "ClienteBase",
    "ClienteCreate",
    "ClienteUpdate",
    "Cliente",
    "EstadoNoticiaBase",
    "EstadoNoticiaCreate",
    "EstadoNoticiaUpdate",
    "EstadoNoticia",
    "ModalidadContactoBase",
    "ModalidadContactoCreate",
    "ModalidadContactoUpdate",
    "ModalidadContacto",
    "SubzonaBase",
    "SubzonaCreate",
    "SubzonaUpdate",
    "Subzona",
    "DetalleProcedenciaBase",
    "DetalleProcedenciaCreate",
    "DetalleProcedenciaUpdate",
    "DetalleProcedencia",
    "MotivoCierreBase",
    "MotivoCierreCreate",
    "MotivoCierreUpdate",
    "MotivoCierre",
    "NoticiaBase",
    "NoticiaCreate",
    "NoticiaUpdate",
    "Noticia",
    "ZonaBase",
    "ZonaCreate",
    "ZonaUpdate",
    "Zona",
]
