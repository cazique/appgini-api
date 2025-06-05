from fastapi import APIRouter

api_router = APIRouter()

from .endpoints import plantilla_pdf as plantilla_pdf_router
from .endpoints import membership_grouppermission as membership_grouppermission_router
from .endpoints import appgini_messages_setting as appgini_messages_setting_router
from .endpoints import inmueble as inmueble_router
from .endpoints import appgini_csv_import_job as appgini_csv_import_job_router
from .endpoints import actividad_encargo as actividad_encargo_router
from .endpoints import appgini_message as appgini_message_router
from .endpoints import subtipologia_inmueble as subtipologia_inmueble_router
from .endpoints import membership_userpermission as membership_userpermission_router
from .endpoints import actividad as actividad_router
from .endpoints import appgini_messages_group_permission as appgini_messages_group_permission_router
from .endpoints import usuario as usuario_router
from .endpoints import tipo_procedencia as tipo_procedencia_router
from .endpoints import encargo as encargo_router
from .endpoints import membership_group as membership_group_router
from .endpoints import estado_contacto as estado_contacto_router
from .endpoints import membership_userrecord as membership_userrecord_router
from .endpoints import estado_encargo as estado_encargo_router
from .endpoints import membership_user as membership_user_router
from .endpoints import agencia as agencia_router
from .endpoints import appgini_query_log_entry as appgini_query_log_entry_router
from .endpoints import tipologia_inmueble as tipologia_inmueble_router
from .endpoints import tipo_actividad as tipo_actividad_router
from .endpoints import direccion as direccion_router
from .endpoints import membership_usersession as membership_usersession_router
from .endpoints import prioridad as prioridad_router
from .endpoints import membership_cache_entry as membership_cache_entry_router
from .endpoints import cliente as cliente_router
from .endpoints import estado_noticia as estado_noticia_router
from .endpoints import modalidad_contacto as modalidad_contacto_router
from .endpoints import subzona as subzona_router
from .endpoints import detalle_procedencia as detalle_procedencia_router
from .endpoints import motivo_cierre as motivo_cierre_router
from .endpoints import noticia as noticia_router
from .endpoints import zona as zona_router

api_router.include_router(plantilla_pdf_router.router, prefix='/plantilla_pdfs', tags=['PlantillaPdf'])
api_router.include_router(membership_grouppermission_router.router, prefix='/membership_grouppermissions', tags=['MembershipGrouppermission'])
api_router.include_router(appgini_messages_setting_router.router, prefix='/appgini_messages_settings', tags=['AppginiMessagesSetting'])
api_router.include_router(inmueble_router.router, prefix='/inmuebles', tags=['Inmueble'])
api_router.include_router(appgini_csv_import_job_router.router, prefix='/appgini_csv_import_jobs', tags=['AppginiCsvImportJob'])
api_router.include_router(actividad_encargo_router.router, prefix='/actividad_encargos', tags=['ActividadEncargo'])
api_router.include_router(appgini_message_router.router, prefix='/appgini_messages', tags=['AppginiMessage'])
api_router.include_router(subtipologia_inmueble_router.router, prefix='/subtipologia_inmuebles', tags=['SubtipologiaInmueble'])
api_router.include_router(membership_userpermission_router.router, prefix='/membership_userpermissions', tags=['MembershipUserpermission'])
api_router.include_router(actividad_router.router, prefix='/actividads', tags=['Actividad'])
api_router.include_router(appgini_messages_group_permission_router.router, prefix='/appgini_messages_group_permissions', tags=['AppginiMessagesGroupPermission'])
api_router.include_router(usuario_router.router, prefix='/usuarios', tags=['Usuario'])
api_router.include_router(tipo_procedencia_router.router, prefix='/tipo_procedencias', tags=['TipoProcedencia'])
api_router.include_router(encargo_router.router, prefix='/encargos', tags=['Encargo'])
api_router.include_router(membership_group_router.router, prefix='/membership_groups', tags=['MembershipGroup'])
api_router.include_router(estado_contacto_router.router, prefix='/estado_contactos', tags=['EstadoContacto'])
api_router.include_router(membership_userrecord_router.router, prefix='/membership_userrecords', tags=['MembershipUserrecord'])
api_router.include_router(estado_encargo_router.router, prefix='/estado_encargos', tags=['EstadoEncargo'])
api_router.include_router(membership_user_router.router, prefix='/membership_users', tags=['MembershipUser'])
api_router.include_router(agencia_router.router, prefix='/agencias', tags=['Agencia'])
api_router.include_router(appgini_query_log_entry_router.router, prefix='/appgini_query_log_entries', tags=['AppginiQueryLogEntry'])
api_router.include_router(tipologia_inmueble_router.router, prefix='/tipologia_inmuebles', tags=['TipologiaInmueble'])
api_router.include_router(tipo_actividad_router.router, prefix='/tipo_actividads', tags=['TipoActividad'])
api_router.include_router(direccion_router.router, prefix='/direccions', tags=['Direccion'])
api_router.include_router(membership_usersession_router.router, prefix='/membership_usersessions', tags=['MembershipUsersession'])
api_router.include_router(prioridad_router.router, prefix='/prioridads', tags=['Prioridad'])
api_router.include_router(membership_cache_entry_router.router, prefix='/membership_cache_entries', tags=['MembershipCacheEntry'])
api_router.include_router(cliente_router.router, prefix='/clientes', tags=['Cliente'])
api_router.include_router(estado_noticia_router.router, prefix='/estado_noticias', tags=['EstadoNoticia'])
api_router.include_router(modalidad_contacto_router.router, prefix='/modalidad_contactos', tags=['ModalidadContacto'])
api_router.include_router(subzona_router.router, prefix='/subzonas', tags=['Subzona'])
api_router.include_router(detalle_procedencia_router.router, prefix='/detalle_procedencias', tags=['DetalleProcedencia'])
api_router.include_router(motivo_cierre_router.router, prefix='/motivo_cierres', tags=['MotivoCierre'])
api_router.include_router(noticia_router.router, prefix='/noticias', tags=['Noticia'])
api_router.include_router(zona_router.router, prefix='/zonas', tags=['Zona'])
