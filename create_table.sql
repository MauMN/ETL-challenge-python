CREATE TABLE IF NOT EXISTS public.tabla_unificada
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cod_localidad integer,
    id_provincia integer,
    id_departamento integer,
    "categoría" text,
    provincia text,
    localidad text,
    nombre text,
    domicilio text,
    "código postal" text,
    "número de teléfono" text,
    mail text,
    web text,
    "Fecha_carga" text
);

CREATE TABLE IF NOT EXISTS public.pantallas_butacas_incaa
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    "Provincia" text,
    "Pantallas" integer,
    "Butacas" integer,
    "espacio_INCAA" integer,
    "Fecha_carga" text
);

CREATE TABLE IF NOT EXISTS public.provincias_fuentes
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fuente text,
    categoria text,
    "Buenos Aires" integer,
    "Catamarca" integer,
    "Chaco" integer,
    "Chubut" integer,
    "Ciudad Autónoma de Buenos Aires" integer,
    "Corrientes" integer,
    "Córdoba" integer,
    "Entre Ríos" integer,
    "Formosa" integer,
    "Jujuy" integer,
    "La Pampa" integer,
    "La Rioja" integer,
    "Mendoza" integer,
    "Misiones" integer,
    "Neuquén" integer,
    "Neuquén " integer,
    "Río Negro" integer,
    "Salta" integer,
    "San Juan" integer,
    "San Luis" integer,
    "Santa Cruz" integer,
    "Santa Fe" integer,
    "Santa Fé" integer,
    "Santiago del Estero" integer,
    "Tierra del Fuego" integer,
    "Tierra del Fuego, Antártida e Islas del Atlántico Sur" integer,
    "Tucumán" integer,
    "Total" integer,
    "Fecha_carga" text
);