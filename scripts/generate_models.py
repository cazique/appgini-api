import os
import sys
import re
import sqlparse # New import
from sqlalchemy import Column, Integer, String, Text, Date, DateTime, Boolean, Numeric # Keep for type reference if needed by get_sqlalchemy_type
from sqlalchemy.dialects.mysql import TINYINT # Keep for type reference

# Output directory for models
OUTPUT_DIR = "app/models/"

# DDL Content (embedding directly for this subtask)
DDL_CONTENT = """
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE DATABASE IF NOT EXISTS `hogarfamiliar_test` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_520_ci;
USE `hogarfamiliar_test`;

DROP TABLE IF EXISTS `actividades`;
CREATE TABLE IF NOT EXISTS `actividades` (
  `actividad_id` varchar(20) NOT NULL,
  `referencia` varchar(30) DEFAULT NULL,
  `usuario_id` varchar(20) DEFAULT NULL,
  `cliente_id` varchar(20) DEFAULT NULL,
  `asunto` varchar(100) NOT NULL,
  `tipo_actividad_id` int(11) DEFAULT NULL,
  `modalidad_contacto_id` int(11) DEFAULT NULL,
  `fecha` date NOT NULL,
  `hora_inicio` time DEFAULT NULL,
  `hora_fin` time DEFAULT NULL,
  `duracion_minutos` int(11) DEFAULT NULL,
  `prioridad_id` int(11) DEFAULT NULL,
  `estado_id` int(11) DEFAULT NULL,
  `descripcion` text DEFAULT NULL,
  `resultado` text DEFAULT NULL,
  `fecha_creacion` datetime DEFAULT NULL,
  `fecha_modificacion` datetime DEFAULT NULL,
  PRIMARY KEY (`actividad_id`),
  KEY `cliente_id` (`cliente_id`),
  KEY `usuario_id` (`usuario_id`),
  KEY `tipo_actividad_id` (`tipo_actividad_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `actividades_encargos`;
CREATE TABLE IF NOT EXISTS `actividades_encargos` (
  `actividad_id` varchar(20) NOT NULL,
  `encargo_id` varchar(20) NOT NULL,
  PRIMARY KEY (`actividad_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `agencias`;
CREATE TABLE IF NOT EXISTS `agencias` (
  `agencia_id` varchar(20) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `direccion` varchar(200) DEFAULT NULL,
  `codigo_postal` varchar(10) DEFAULT NULL,
  `localidad` varchar(50) DEFAULT NULL,
  `provincia` varchar(50) DEFAULT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `responsable_id` varchar(20) DEFAULT NULL,
  `fecha_alta` date DEFAULT NULL,
  `activo` tinyint(1) DEFAULT 1,
  PRIMARY KEY (`agencia_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `appgini_csv_import_jobs`;
CREATE TABLE IF NOT EXISTS `appgini_csv_import_jobs` (
  `id` varchar(40) NOT NULL,
  `memberID` varchar(100) NOT NULL,
  `config` text DEFAULT NULL,
  `insert_ts` int(11) DEFAULT NULL,
  `last_update_ts` int(11) DEFAULT NULL,
  `total` int(11) DEFAULT 99999999,
  `done` int(11) DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `appgini_messages`;
CREATE TABLE IF NOT EXISTS `appgini_messages` (
  `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `originalId` bigint(20) UNSIGNED DEFAULT NULL,
  `createdTS` int(10) UNSIGNED NOT NULL,
  `draft` tinyint(4) NOT NULL DEFAULT 1,
  `sentTS` int(10) UNSIGNED DEFAULT NULL,
  `seenTS` int(10) UNSIGNED DEFAULT NULL,
  `inReplyTo` bigint(20) UNSIGNED DEFAULT NULL,
  `sender` varchar(200) NOT NULL,
  `owner` varchar(200) DEFAULT NULL,
  `recipients` text DEFAULT NULL,
  `subject` varchar(100) NOT NULL,
  `message` text DEFAULT NULL,
  `markedUnread` tinyint(4) NOT NULL DEFAULT 1,
  `starred` tinyint(4) NOT NULL DEFAULT 0,
  `updateDT` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

DROP TABLE IF EXISTS `appgini_messages_group_permissions`;
CREATE TABLE IF NOT EXISTS `appgini_messages_group_permissions` (
  `groupID` int(10) UNSIGNED NOT NULL,
  `hasAccess` tinyint(4) NOT NULL DEFAULT 0,
  `allowedRecipientGroupIDs` text DEFAULT NULL,
  `canSendGroupMessage` tinyint(4) NOT NULL DEFAULT 0,
  `canSendGlobalMessage` tinyint(4) NOT NULL DEFAULT 0,
  `maxRecipients` int(10) UNSIGNED DEFAULT 1,
  PRIMARY KEY (`groupID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

DROP TABLE IF EXISTS `appgini_messages_settings`;
CREATE TABLE IF NOT EXISTS `appgini_messages_settings` (
  `key` varchar(100) NOT NULL,
  `value` text DEFAULT NULL,
  PRIMARY KEY (`key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

DROP TABLE IF EXISTS `appgini_query_log`;
CREATE TABLE IF NOT EXISTS `appgini_query_log` (
  `datetime` timestamp NOT NULL DEFAULT current_timestamp(),
  `statement` longtext DEFAULT NULL,
  `duration` decimal(10,2) UNSIGNED DEFAULT 0.00,
  `error` text DEFAULT NULL,
  `memberID` varchar(200) DEFAULT NULL,
  `uri` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `clientes`;
CREATE TABLE IF NOT EXISTS `clientes` (
  `cliente_id` varchar(20) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellidos` varchar(100) NOT NULL,
  `nombre_completo` varchar(150) DEFAULT NULL,
  `tratamiento` varchar(10) DEFAULT NULL,
  `genero` varchar(40) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `documento_id` varchar(20) DEFAULT NULL,
  `nacionalidad` varchar(50) DEFAULT NULL,
  `estado_civil` varchar(30) DEFAULT NULL,
  `telefono_fijo` varchar(15) DEFAULT NULL,
  `telefono_movil` varchar(15) DEFAULT NULL,
  `telefono_adicional` varchar(15) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `cliente_telefonico` tinyint(1) DEFAULT 0,
  `profesion` varchar(100) DEFAULT NULL,
  `sector_actividad` varchar(100) DEFAULT NULL,
  `empresa` varchar(100) DEFAULT NULL,
  `fecha_alta` date DEFAULT NULL,
  `ultima_modificacion` datetime DEFAULT NULL,
  `agencia_id` varchar(20) DEFAULT NULL,
  `usuario_id` varchar(20) DEFAULT NULL,
  `observaciones` text DEFAULT NULL,
  PRIMARY KEY (`cliente_id`),
  UNIQUE KEY `documento_id` (`documento_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `detalles_procedencia`;
CREATE TABLE IF NOT EXISTS `detalles_procedencia` (
  `detalle_procedencia_id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo_procedencia_id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`detalle_procedencia_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `direcciones`;
CREATE TABLE IF NOT EXISTS `direcciones` (
  `direccion_id` int(11) NOT NULL AUTO_INCREMENT,
  `cliente_id` varchar(20) DEFAULT NULL,
  `inmueble_id` varchar(20) DEFAULT NULL,
  `tipo_direccion` varchar(40) NOT NULL,
  `calle` varchar(100) NOT NULL,
  `numero` varchar(10) DEFAULT NULL,
  `piso` varchar(10) DEFAULT NULL,
  `puerta` varchar(10) DEFAULT NULL,
  `escalera` varchar(10) DEFAULT NULL,
  `codigo_postal` varchar(10) DEFAULT NULL,
  `localidad` varchar(50) NOT NULL,
  `provincia` varchar(50) NOT NULL,
  `pais` varchar(50) DEFAULT 'Espana',
  `referencia_catastral` varchar(50) DEFAULT NULL,
  `coordenadas_latitud` decimal(10,8) DEFAULT NULL,
  `coordenadas_longitud` decimal(11,8) DEFAULT NULL,
  `principal` tinyint(1) DEFAULT 0,
  `fecha_alta` datetime DEFAULT NULL,
  `ultima_modificacion` datetime DEFAULT NULL,
  PRIMARY KEY (`direccion_id`),
  KEY `cliente_id` (`cliente_id`),
  KEY `inmueble_id` (`inmueble_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `encargos`;
CREATE TABLE IF NOT EXISTS `encargos` (
  `encargo_id` varchar(20) NOT NULL,
  `referencia` varchar(30) DEFAULT NULL,
  `inmueble_id` varchar(20) NOT NULL,
  `propietario_id` varchar(20) NOT NULL,
  `estado_id` int(11) NOT NULL,
  `estado_contacto_id` int(11) DEFAULT NULL,
  `motivo` varchar(40) NOT NULL,
  `tipo_procedencia_id` int(11) DEFAULT NULL,
  `precio` decimal(12,2) NOT NULL,
  `precio_parking_incluido` tinyint(1) DEFAULT 0,
  `valoracion` decimal(12,2) DEFAULT NULL,
  `valoracion_solo_inmueble` decimal(12,2) DEFAULT NULL,
  `nuda_propiedad` tinyint(1) DEFAULT 0,
  `tratabilidad` tinyint(4) DEFAULT NULL,
  `fecha_creacion` datetime DEFAULT NULL,
  `fecha_modificacion` datetime DEFAULT NULL,
  `fecha_cierre` date DEFAULT NULL,
  `motivo_cierre_id` int(11) DEFAULT NULL,
  `fecha_ultima_cita` date DEFAULT NULL,
  `fecha_ultima_actividad` date DEFAULT NULL,
  `fecha_ultimo_contacto` date DEFAULT NULL,
  `nota_privada` text DEFAULT NULL,
  `llaves_oficina` tinyint(1) DEFAULT 0,
  PRIMARY KEY (`encargo_id`),
  KEY `inmueble_id` (`inmueble_id`),
  KEY `propietario_id` (`propietario_id`),
  KEY `estado_id` (`estado_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `estados_contacto`;
CREATE TABLE IF NOT EXISTS `estados_contacto` (
  `estado_contacto_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  `dias_inactividad_min` int(11) DEFAULT 0,
  `dias_inactividad_max` int(11) DEFAULT 999,
  `orden` tinyint(4) DEFAULT 0,
  `color` varchar(7) DEFAULT '#000000',
  PRIMARY KEY (`estado_contacto_id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `estados_encargo`;
CREATE TABLE IF NOT EXISTS `estados_encargo` (
  `estado_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  `orden` tinyint(4) DEFAULT 0,
  `color` varchar(7) DEFAULT '#000000',
  PRIMARY KEY (`estado_id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `estados_noticia`;
CREATE TABLE IF NOT EXISTS `estados_noticia` (
  `estado_noticia_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  `orden` tinyint(4) DEFAULT 0,
  `color` varchar(7) DEFAULT '#000000',
  PRIMARY KEY (`estado_noticia_id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `inmuebles`;
CREATE TABLE IF NOT EXISTS `inmuebles` (
  `inmueble_id` varchar(20) NOT NULL,
  `referencia` varchar(30) DEFAULT NULL,
  `propietario_id` varchar(20) DEFAULT NULL,
  `estado` varchar(40) DEFAULT 'Disponible',
  `tipologia_id` int(11) DEFAULT NULL,
  `subtipologia_id` int(11) DEFAULT NULL,
  `direccion_id` int(11) DEFAULT NULL,
  `zona_id` int(11) DEFAULT NULL,
  `dormitorios` tinyint(4) DEFAULT NULL,
  `banos` tinyint(4) DEFAULT NULL,
  `aseos` tinyint(4) DEFAULT NULL,
  `m2_utiles` decimal(8,2) DEFAULT NULL,
  `m2_construidos` decimal(8,2) DEFAULT NULL,
  `m2_terraza` decimal(8,2) DEFAULT NULL,
  `altura` varchar(20) DEFAULT NULL,
  `orientacion` varchar(30) DEFAULT NULL,
  `estado_conservacion` varchar(30) DEFAULT NULL,
  `ano_construccion` smallint(6) DEFAULT NULL,
  `ano_reforma` smallint(6) DEFAULT NULL,
  `ascensor` tinyint(1) DEFAULT 0,
  `terraza` tinyint(1) DEFAULT 0,
  `balcon` tinyint(1) DEFAULT 0,
  `garaje` tinyint(1) DEFAULT 0,
  `trastero` tinyint(1) DEFAULT 0,
  `calefaccion_tipo` varchar(50) DEFAULT NULL,
  `climatizacion` varchar(50) DEFAULT NULL,
  `certificado_energetico` varchar(5) DEFAULT NULL,
  `consumo_energetico` decimal(8,2) DEFAULT NULL,
  `emisiones_co2` decimal(8,2) DEFAULT NULL,
  `referencia_catastral` varchar(50) DEFAULT NULL,
  `fecha_alta` datetime DEFAULT NULL,
  `ultima_modificacion` datetime DEFAULT NULL,
  `llaves_oficina` tinyint(1) DEFAULT 0,
  `notas_privadas` text DEFAULT NULL,
  `observaciones` text DEFAULT NULL,
  PRIMARY KEY (`inmueble_id`),
  KEY `propietario_id` (`propietario_id`),
  KEY `tipologia_id` (`tipologia_id`),
  UNIQUE KEY `direccion_id_unique` (`direccion_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `membership_cache`;
CREATE TABLE IF NOT EXISTS `membership_cache` (
  `request` varchar(100) NOT NULL,
  `request_ts` int(11) DEFAULT NULL,
  `response` longtext DEFAULT NULL,
  PRIMARY KEY (`request`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `membership_grouppermissions`;
CREATE TABLE IF NOT EXISTS `membership_grouppermissions` (
  `permissionID` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `groupID` int(10) UNSIGNED DEFAULT NULL,
  `tableName` varchar(100) DEFAULT NULL,
  `allowInsert` tinyint(4) NOT NULL DEFAULT 0,
  `allowView` tinyint(4) NOT NULL DEFAULT 0,
  `allowEdit` tinyint(4) NOT NULL DEFAULT 0,
  `allowDelete` tinyint(4) NOT NULL DEFAULT 0,
  PRIMARY KEY (`permissionID`),
  UNIQUE KEY `groupID_tableName` (`groupID`,`tableName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `membership_groups`;
CREATE TABLE IF NOT EXISTS `membership_groups` (
  `groupID` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` text DEFAULT NULL,
  `allowSignup` tinyint(4) DEFAULT NULL,
  `needsApproval` tinyint(4) DEFAULT NULL,
  `allowCSVImport` tinyint(4) NOT NULL DEFAULT 0,
  PRIMARY KEY (`groupID`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `membership_userpermissions`;
CREATE TABLE IF NOT EXISTS `membership_userpermissions` (
  `permissionID` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `memberID` varchar(100) NOT NULL,
  `tableName` varchar(100) DEFAULT NULL,
  `allowInsert` tinyint(4) NOT NULL DEFAULT 0,
  `allowView` tinyint(4) NOT NULL DEFAULT 0,
  `allowEdit` tinyint(4) NOT NULL DEFAULT 0,
  `allowDelete` tinyint(4) NOT NULL DEFAULT 0,
  PRIMARY KEY (`permissionID`),
  UNIQUE KEY `memberID_tableName` (`memberID`,`tableName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `membership_userrecords`;
CREATE TABLE IF NOT EXISTS `membership_userrecords` (
  `recID` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `tableName` varchar(100) DEFAULT NULL,
  `pkValue` varchar(255) DEFAULT NULL,
  `memberID` varchar(100) DEFAULT NULL,
  `dateAdded` bigint(20) UNSIGNED DEFAULT NULL,
  `dateUpdated` bigint(20) UNSIGNED DEFAULT NULL,
  `groupID` int(10) UNSIGNED DEFAULT NULL,
  PRIMARY KEY (`recID`),
  UNIQUE KEY `tableName_pkValue` (`tableName`,`pkValue`(100)),
  KEY `pkValue` (`pkValue`),
  KEY `tableName` (`tableName`),
  KEY `memberID` (`memberID`),
  KEY `groupID` (`groupID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `membership_users`;
CREATE TABLE IF NOT EXISTS `membership_users` (
  `memberID` varchar(100) NOT NULL,
  `passMD5` varchar(255) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `signupDate` date DEFAULT NULL,
  `groupID` int(10) UNSIGNED DEFAULT NULL,
  `isBanned` tinyint(4) DEFAULT NULL,
  `isApproved` tinyint(4) DEFAULT NULL,
  `custom1` text DEFAULT NULL,
  `custom2` text DEFAULT NULL,
  `custom3` text DEFAULT NULL,
  `custom4` text DEFAULT NULL,
  `comments` text DEFAULT NULL,
  `pass_reset_key` varchar(100) DEFAULT NULL,
  `pass_reset_expiry` int(10) UNSIGNED DEFAULT NULL,
  `flags` text DEFAULT NULL,
  `allowCSVImport` tinyint(4) NOT NULL DEFAULT 0,
  `data` longtext DEFAULT NULL,
  PRIMARY KEY (`memberID`),
  KEY `groupID` (`groupID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `membership_usersessions`;
CREATE TABLE IF NOT EXISTS `membership_usersessions` (
  `memberID` varchar(100) NOT NULL,
  `token` varchar(100) NOT NULL,
  `agent` varchar(100) NOT NULL,
  `expiry_ts` int(10) UNSIGNED NOT NULL,
  UNIQUE KEY `memberID_token_agent` (`memberID`,`token`(50),`agent`(50)),
  KEY `memberID` (`memberID`),
  KEY `expiry_ts` (`expiry_ts`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

DROP TABLE IF EXISTS `modalidades_contacto`;
CREATE TABLE IF NOT EXISTS `modalidades_contacto` (
  `modalidad_contacto_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`modalidad_contacto_id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `motivos_cierre`;
CREATE TABLE IF NOT EXISTS `motivos_cierre` (
  `motivo_cierre_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  `es_positivo` tinyint(1) DEFAULT 0,
  PRIMARY KEY (`motivo_cierre_id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `noticias`;
CREATE TABLE IF NOT EXISTS `noticias` (
  `noticia_id` varchar(20) NOT NULL,
  `referencia` varchar(30) DEFAULT NULL,
  `inmueble_id` varchar(20) DEFAULT NULL,
  `cliente_id` varchar(20) DEFAULT NULL,
  `colaborador_id` varchar(20) DEFAULT NULL,
  `estado_noticia_id` int(11) DEFAULT NULL,
  `estado_contacto_id` int(11) DEFAULT NULL,
  `tipo_procedencia_id` int(11) DEFAULT NULL,
  `detalle_procedencia_id` int(11) DEFAULT NULL,
  `motivacion` varchar(40) NOT NULL,
  `valoracion` decimal(12,2) DEFAULT NULL,
  `valoracion_solo_inmueble` decimal(12,2) DEFAULT NULL,
  `precio_pedido` decimal(12,2) DEFAULT NULL,
  `fecha_valoracion` date DEFAULT NULL,
  `fecha_estimacion_interna` date DEFAULT NULL,
  `fecha_ultima_cita` date DEFAULT NULL,
  `fecha_ultimo_contacto` date DEFAULT NULL,
  `fecha_cierre` date DEFAULT NULL,
  `motivo_cierre_id` int(11) DEFAULT NULL,
  `nota` text DEFAULT NULL,
  `fecha_creacion` datetime DEFAULT NULL,
  `fecha_modificacion` datetime DEFAULT NULL,
  PRIMARY KEY (`noticia_id`),
  KEY `cliente_id` (`cliente_id`),
  KEY `inmueble_id` (`inmueble_id`),
  KEY `estado_noticia_id` (`estado_noticia_id`),
  KEY `colaborador_id` (`colaborador_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `plantillas_pdf`;
CREATE TABLE IF NOT EXISTS `plantillas_pdf` (
  `nombre` varchar(255) DEFAULT NULL,
  `tabla` varchar(255) DEFAULT NULL,
  `html` varchar(255) DEFAULT NULL,
  `grupo_autorizado` varchar(255) DEFAULT NULL,
  `usuario_id` varchar(255) DEFAULT NULL,
  `zona_id` int(11) NOT NULL AUTO_INCREMENT,
  `fecha_creacion` datetime DEFAULT NULL,
  `fecha_modificacion` datetime DEFAULT NULL,
  `nota` text DEFAULT NULL,
  PRIMARY KEY (`zona_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

DROP TABLE IF EXISTS `prioridades`;
CREATE TABLE IF NOT EXISTS `prioridades` (
  `prioridad_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  `orden` tinyint(4) DEFAULT 0,
  `color` varchar(7) DEFAULT '#000000',
  PRIMARY KEY (`prioridad_id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `subtipologias_inmueble`;
CREATE TABLE IF NOT EXISTS `subtipologias_inmueble` (
  `subtipologia_id` int(11) NOT NULL AUTO_INCREMENT,
  `tipologia_id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`subtipologia_id`),
  KEY `tipologia_id` (`tipologia_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `subzonas`;
CREATE TABLE IF NOT EXISTS `subzonas` (
  `subzona_id` int(11) NOT NULL AUTO_INCREMENT,
  `zona_id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`subzona_id`),
  KEY `zona_id` (`zona_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `tipologias_inmueble`;
CREATE TABLE IF NOT EXISTS `tipologias_inmueble` (
  `tipologia_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`tipologia_id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `tipos_actividad`;
CREATE TABLE IF NOT EXISTS `tipos_actividad` (
  `tipo_actividad_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  `requiere_resultado` tinyint(1) DEFAULT 0,
  PRIMARY KEY (`tipo_actividad_id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `tipos_procedencia`;
CREATE TABLE IF NOT EXISTS `tipos_procedencia` (
  `tipo_procedencia_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`tipo_procedencia_id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE IF NOT EXISTS `usuarios` (
  `usuario_id` varchar(20) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellidos` varchar(100) NOT NULL,
  `nombre_completo` varchar(150) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  `puesto` varchar(50) DEFAULT NULL,
  `agencia_id` varchar(20) DEFAULT NULL,
  `activo` tinyint(1) DEFAULT 1,
  `fecha_alta` date DEFAULT NULL,
  `ultima_conexion` datetime DEFAULT NULL,
  PRIMARY KEY (`usuario_id`),
  UNIQUE KEY `email` (`email`),
  KEY `agencia_id` (`agencia_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;

DROP TABLE IF EXISTS `zonas`;
CREATE TABLE IF NOT EXISTS `zonas` (
  `zona_id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `localidad` varchar(50) NOT NULL,
  `provincia` varchar(50) NOT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`zona_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_520_ci;
COMMIT;
"""

def to_camel_case(name):
    """Converts snake_case or spaced names to CamelCase."""
    return "".join(word.capitalize() for word in re.split('_| ', name))

def parse_sql_type_to_sqlalchemy(sql_type_str):
    """Converts SQL type string from DDL to SQLAlchemy type string."""
    sql_type_str = sql_type_str.lower()

    if sql_type_str.startswith("varchar"):
        length = re.search(r'\((\d+)\)', sql_type_str)
        return f"String({length.group(1)})" if length else "String"
    elif sql_type_str.startswith("int") or sql_type_str.startswith("bigint") or sql_type_str.startswith("smallint"):
        return "Integer"
    elif sql_type_str == "text" or sql_type_str == "longtext":
        return "Text"
    elif sql_type_str == "date":
        return "Date"
    elif sql_type_str == "datetime" or sql_type_str == "timestamp":
        return "DateTime"
    elif sql_type_str.startswith("tinyint(1)") or sql_type_str == "boolean": # boolean might not appear in this DDL
        return "Boolean"
    elif sql_type_str.startswith("tinyint"): # other tinyints
        return "Integer" # Or SmallInteger if preferred for TINYINT > 1
    elif sql_type_str.startswith("decimal"):
        match = re.search(r'\((\d+),(\d+)\)', sql_type_str)
        if match:
            return f"Numeric({match.group(1)}, {match.group(2)})"
        return "Numeric"
    elif sql_type_str.startswith("time"):
        return "Time" # Add Time type
    else:
        print(f"Warning: Unhandled SQL type: {sql_type_str}. Defaulting to String. Please review manually.")
        return "String"

def generate_models_from_ddl(ddl_sql):
    """Generates SQLAlchemy models from DDL SQL statements."""
    parsed = sqlparse.parse(ddl_sql)

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    init_py_path = os.path.join(OUTPUT_DIR, "__init__.py")
    with open(init_py_path, "w") as f:
        f.write("# This file makes Python treat the directory `models` as a package.\n")
        f.write("# It's managed by scripts/generate_models.py\n\n")
        f.write("from .database import Base, engine, SessionLocal, get_db\n\n")

    all_table_names_for_init = []

    for stmt in parsed:
        if stmt.get_type() == 'CREATE':
            # Further check if it's a CREATE TABLE statement
            # Check for comment types
            is_comment_token = lambda t: t.ttype in (sqlparse.tokens.Comment.Single, sqlparse.tokens.Comment.Multiline)
            tokens = [t.value.lower() for t in stmt.tokens if t.ttype is not sqlparse.tokens.Whitespace and not is_comment_token(t)]
            if not ('table' in tokens):
                continue

            table_name = None
            columns = []
            primary_keys = set()
            unique_constraints = {} # Store as dict: constraint_name -> list of columns
            indexes = {} # Store as dict: index_name -> list of columns

            # Find table name
            for token in stmt.tokens:
                if isinstance(token, sqlparse.sql.Identifier):
                    table_name = token.get_real_name()
                    break

            if not table_name:
                continue

            all_table_names_for_init.append(table_name)
            class_name = to_camel_case(table_name)
            print(f"Processing table: {table_name} -> class {class_name}")

            # Find columns within parentheses
            par_level = 0
            in_column_defs = False
            for token in stmt.tokens:
                if token.is_group and isinstance(token, sqlparse.sql.Parenthesis): # This is the main ( ... ) block
                    # Iterate over tokens within the main parenthesis block
                    definitions_str = "".join(str(t) for t in token.tokens[1:-1]) # Content between ( and )
                    # Split by comma, but be careful about commas inside type definitions e.g. DECIMAL(10,2)
                    # sqlparse can help better here by further parsing the content of parenthesis

                    # A simplified splitting logic for now, might need refinement
                    # This regex tries to split by comma, unless the comma is within parentheses
                    raw_defs = re.split(r',\s*(?![^()]*\))', definitions_str.strip())

                    for part in raw_defs:
                        part = part.strip()
                        if not part: continue

                        # Check for PRIMARY KEY, UNIQUE KEY, KEY definitions
                        if part.lower().startswith("primary key"):
                            pk_match = re.search(r'\((.*?)\)', part, re.IGNORECASE)
                            if pk_match:
                                pks = [col.strip().replace('`', '') for col in pk_match.group(1).split(',')]
                                primary_keys.update(pks)
                        elif part.lower().startswith("unique key"):
                            uk_match = re.search(r'`(.*?)`\s*\((.*?)\)', part, re.IGNORECASE) # `constraint_name` (`col1`, `col2`)
                            if uk_match:
                                constraint_name = uk_match.group(1)
                                cols = [col.strip().replace('`', '') for col in uk_match.group(2).split(',')]
                                unique_constraints[constraint_name] = cols
                        elif part.lower().startswith("key"): # Simple index
                            idx_match = re.search(r'`(.*?)`\s*\((.*?)\)', part, re.IGNORECASE) # `index_name` (`col1`, `col2`)
                            if idx_match:
                                index_name = idx_match.group(1)
                                cols = [col.strip().replace('`', '') for col in idx_match.group(2).split(',')]
                                indexes[index_name] = cols
                        else: # Assume column definition
                            col_tokens = part.split()
                            # Basic check: needs at least name and type. Otherwise, skip.
                            if len(col_tokens) < 2:
                                print(f"Skipping part, not enough tokens for col name/type: '{part}'")
                                continue
                            col_name = col_tokens[0].replace('`', '')
                            sql_type = col_tokens[1] # This was the failing line. Now guarded by len check.

                            # Attempt to reconstruct sql_type if it was split from its parameters e.g. "INT (11)"
                            # This is a simplified approach. A full SQL parser would handle this more gracefully.
                            idx = 2
                            while idx < len(col_tokens):
                                # If the next token starts with '(' or is 'UNSIGNED' (common type modifiers)
                                # append it to sql_type. This is a heuristic.
                                if col_tokens[idx].startswith("(") or col_tokens[idx].lower() == "unsigned":
                                    sql_type += " " + col_tokens[idx]
                                    idx += 1
                                else:
                                    # If it's something else, assume it's not part of the type definition
                                    break

                            # Handle type parameters like VARCHAR(255) or DECIMAL(10,2)
                            if '(' in sql_type and ')' in sql_type:
                                type_def_match = re.match(r'([a-zA-Z_]+)\((.*?)\)', sql_type)
                                if type_def_match:
                                     # keep the (..) part for parse_sql_type_to_sqlalchemy
                                     pass # sql_type is already good
                                else: # fallback if regex fails
                                     if len(col_tokens) > 2 and '(' in col_tokens[2]:
                                        sql_type += col_tokens[2]


                            is_nullable = "not null" not in part.lower()
                            is_auto_increment = "auto_increment" in part.lower()

                            default_value_match = re.search(r"default\s+(.*?)(?:\s+not\s+null|\s+null|\s*$)", part, re.IGNORECASE)
                            default_value = None
                            if default_value_match:
                                default_value = default_value_match.group(1).strip("'")
                                if default_value.lower() == 'null': # Explicit DEFAULT NULL
                                    default_value = None
                                    is_nullable = True
                                elif default_value.lower() == 'current_timestamp()':
                                     default_value = "func.now()" # For SQLAlchemy
                                elif default_value.lower() == 'current_timestamp': # MariaDB/MySQL variant
                                     default_value = "func.now()"


                            columns.append({
                                "name": col_name,
                                "type_str": sql_type,
                                "nullable": is_nullable,
                                "primary_key": False, # Will be set later from PRIMARY KEY clause
                                "unique": False, # Will be set later
                                "index": False, # Will be set later
                                "auto_increment": is_auto_increment,
                                "default": default_value
                            })
                    break # Processed the main parenthesis block

            # Post-process columns based on PK, UNIQUE, KEY constraints
            for col_def in columns:
                if col_def["name"] in primary_keys:
                    col_def["primary_key"] = True
                    col_def["nullable"] = False # PKs are implicitly not null

                for constraint_cols in unique_constraints.values():
                    if col_def["name"] in constraint_cols:
                        col_def["unique"] = True # Mark as unique if part of any unique constraint
                        break

                # Simple index check (note: PKs and UNIQUE constraints often create indexes automatically)
                for index_cols in indexes.values():
                     if col_def["name"] in index_cols:
                        col_def["index"] = True
                        break


            # Add a dummy primary key if none were found from DDL
            if not primary_keys and not any(col.get("primary_key") for col in columns):
                print(f"Warning: No primary key found for table {table_name}. Adding a dummy 'id' primary key for ORM compatibility.")
                columns.insert(0, { # Insert at the beginning
                    "name": "id",
                    "type_str": "int", # Simple integer type
                    "nullable": False,
                    "primary_key": True,
                    "unique": False,
                    "index": False,
                    "auto_increment": True, # Common for dummy PKs
                    "default": None
                })
                primary_keys.add("id") # Register it as a PK

            # Write model file
            model_file_path = os.path.join(OUTPUT_DIR, f"{table_name}.py")
            with open(model_file_path, "w") as f:
                f.write("from sqlalchemy import Column, Integer, String, Text, Date, DateTime, Boolean, Numeric, ForeignKey, Time, func\n") # Added Time, func
                f.write("from sqlalchemy.orm import relationship\n")
                f.write("from .database import Base\n\n")
                f.write(f"class {class_name}(Base):\n")
                f.write(f"    __tablename__ = \"{table_name}\"\n\n")

                for col in columns:
                    sa_type = parse_sql_type_to_sqlalchemy(col["type_str"])
                    attrs = []
                    if col["primary_key"]:
                        attrs.append("primary_key=True")
                    if not col["nullable"] and not col["primary_key"]: # PKs are already not nullable
                        attrs.append("nullable=False")
                    if col["unique"] and not col["primary_key"]: # PK implies unique usually
                         # Only add if it's a single-column unique constraint identified directly on the column,
                         # or if it's the first column of a multi-column unique constraint.
                         # More robust unique constraint handling for multi-column uniques should be done at table level via UniqueConstraint
                         is_part_of_multi_col_unique = False
                         for constraint_cols in unique_constraints.values(): # Corrected typo here
                             if col["name"] in constraint_cols and len(constraint_cols) > 1:
                                 is_part_of_multi_col_unique = True
                                 break
                         if not is_part_of_multi_col_unique:
                            attrs.append("unique=True")

                    # Add index=True if it's indexed, not a PK, and not unique (unique constraints often imply an index)
                    if col["index"] and not col["primary_key"] and not col["unique"]:
                        attrs.append("index=True")

                    if col["auto_increment"]:
                        attrs.append("autoincrement=True")

                    if col["default"] is not None:
                        if col["default"] == "func.now()":
                            attrs.append(f"server_default={col['default']}")
                        else: # String literal default
                            attrs.append(f"default='{col['default']}'")


                    f.write(f"    {col['name']} = Column({sa_type}")
                    if attrs:
                        f.write(", " + ", ".join(attrs))
                    f.write(")\n")

                f.write("\n    # TODO: Define relationships here. For example:\n")
                f.write(f"    # items = relationship(\"Item\", back_populates=\"{table_name}_owner\") # Adjust as necessary\n")

                pk_col_name = columns[0]['name'] # Default to first col for repr if no PK
                for col in columns:
                    if col['primary_key']:
                        pk_col_name = col['name']
                        break

                f.write("\n    def __repr__(self):\n")
                f.write(f"        return f\"<{class_name} {pk_col_name}={{getattr(self, '{pk_col_name}', 'N/A')}}>\"\n")

            print(f"Generated model for table {table_name} in {model_file_path}")

    # Update app/models/__init__.py to import all generated models
    with open(init_py_path, "a") as f:
        f.write("\n# Import all generated models for easier access\n")
        if not all_table_names_for_init:
            f.write("# No tables found in DDL to generate models.\n")
        else:
            for tbl_name in all_table_names_for_init:
                class_name_for_import = to_camel_case(tbl_name)
                f.write(f"from .{tbl_name} import {class_name_for_import}\n")
    print(f"Updated {init_py_path} with all model imports.")


if __name__ == "__main__":
    print("Starting model generation from DDL...")
    # For now, DDL_CONTENT is embedded. Future: allow file path argument.
    if not DDL_CONTENT:
        print("Error: DDL_CONTENT is empty. Cannot generate models.")
        # sys.exit(1) # Allow script to continue to test part if DDL is empty but files exist

    # --- Temporarily disable DDL parsing and model file generation ---
    # generate_models_from_ddl(DDL_CONTENT)
    # print("Script finished. Models generated from DDL.")
    # print(f"Generated models are in: {os.path.abspath(OUTPUT_DIR)}")
    # print("IMPORTANT: Review generated models for correctness, especially ForeignKeys and relationships, as DDL parsing has limitations.")
    print("Skipping DDL parsing and model file generation for this run.")
    # --- End of temporary disable ---

    # --- Optional: Test schema creation ---
    try:
        print("\nAttempting to create schema in-memory (SQLite)...")
        import sys
        import os
        # Add the repository root to sys.path to allow 'import app.models'
        SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
        REPO_ROOT = os.path.dirname(SCRIPT_DIR)
        if REPO_ROOT not in sys.path:
            sys.path.insert(0, REPO_ROOT)

        from sqlalchemy import create_engine
        from app.models.database import Base # Now this should work

        # Import all model classes from app.models to ensure they are registered with Base
        # This relies on app/models/__init__.py importing all of them.
        import app.models # This should trigger imports from app.models.__init__

        # Create an in-memory SQLite engine for testing
        test_engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(test_engine)
        print("Schema creation successful with SQLite in-memory!")
    except Exception as e:
        print(f"Error during schema creation test: {e}")
        print("This indicates potential issues in model definitions (FKs, relationships, imports).")
    # --- End of optional test ---

"""
DETAILED EXPLANATION of DDL parsing logic added:
- `generate_models_from_ddl(ddl_sql)`: New main function.
- `sqlparse.parse(ddl_sql)`: Parses the entire DDL.
- Iterates statements, looking for `CREATE TABLE`.
- Extracts table name using `sqlparse.sql.Identifier`.
- Column parsing:
    - It looks for the main `(...)` block of the `CREATE TABLE` statement.
    - It then tries to split the content of this block by commas. This is a simplification. A robust parser would use `sqlparse` more deeply to tokenize individual column definitions and constraints. Current regex `r',\s*(?![^()]*\))'` is a common way to split by comma not inside parentheses.
    - For each part (column def or constraint):
        - If `PRIMARY KEY`, extracts column names.
        - If `UNIQUE KEY`, extracts constraint name and column names.
        - If `KEY` (index), extracts index name and column names.
        - Otherwise, assumes it's a column definition:
            - Splits by space to get name, type, and other attributes like `NOT NULL`, `AUTO_INCREMENT`, `DEFAULT`.
            - `parse_sql_type_to_sqlalchemy` is used to map SQL type string to SQLAlchemy type string.
- Post-processing: After collecting all column definitions and constraints:
    - Marks columns as `primary_key=True` and `nullable=False` if they are in the `primary_keys` set.
    - Marks columns as `unique=True` if they are part of any `unique_constraints`.
    - Marks columns as `index=True` if they are part of any `indexes`.
- Model file writing: Similar to before, but uses the parsed information.
  - Includes `Time` and `func` in imports for SQLAlchemy.
  - Handles `default` values, including `func.now()` for `CURRENT_TIMESTAMP`.
- `__init__.py` update: Similar to before.
- `if __name__ == "__main__":` calls `generate_models_from_ddl`.
- Added `Time` to `parse_sql_type_to_sqlalchemy`.
Limitations:
- The DDL parser is relatively basic. It relies on string splitting and regex for column definitions and constraints within the `CREATE TABLE (...)` block. Complex definitions or edge cases in SQL syntax might not be parsed correctly.
- Foreign Key Constraints: The current DDL provided does not have explicit `FOREIGN KEY ... REFERENCES ...` clauses within the `CREATE TABLE` statements for most relations (they are often implied by `KEY col_name (col_name)` and naming conventions). The parser has a placeholder for FKs but won't find many in *this specific DDL*. FKs and relationships will largely need to be added manually in the next step, as per the subtask description.
- Character sets, collations, engine types are ignored for SQLAlchemy model generation.
- `UNSIGNED` attribute for integers is noted in DDL but not directly translated to a standard SQLAlchemy type constraint (SQLAlchemy integers handle various sizes; specific dialects might have unsigned types).
"""
