"""Normalización y unificación de los datos proveninetes de las 3 fuentes en tabla común"""
import numpy as np
import pandas as pd
from extract import dia, mes1, año, museos_path, salas_path, biblios_path

df_museos = pd.read_csv('{}/museos-{}-{}-{}.csv'.format(museos_path, dia, mes1, año))
df_salas = pd.read_csv('{}/salas-{}-{}-{}.csv'.format(salas_path, dia, mes1, año))
df_bibliotecas = pd.read_csv('{}/bibliotecas-{}-{}-{}.csv'.format(biblios_path, dia, mes1, año))

df_museos_clean = df_museos[
    ['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'categoria', 'provincia', 'localidad', 'nombre', 'direccion', 'CP',
     'telefono', 'Mail', 'Web']]
df_salas_clean = df_salas[
    ['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'Categoría', 'Provincia', 'Localidad', 'Nombre', 'Dirección', 'CP',
     'Teléfono', 'Mail', 'Web']]
df_bibliotecas_clean = df_bibliotecas[
    ['Cod_Loc', 'IdProvincia', 'IdDepartamento', 'Categoría', 'Provincia', 'Localidad', 'Nombre', 'Domicilio', 'CP',
     'Teléfono', 'Mail', 'Web']]

df_museos_clean = df_museos_clean.rename(
    columns={'Cod_Loc': 'cod_localidad', 'IdProvincia': 'id_provincia', 'IdDepartamento': 'id_departamento',
             'categoria': 'categoría',
             'direccion': 'domicilio', 'CP': 'código postal', 'telefono': 'número de teléfono', 'Mail': 'mail',
             'Web': 'web'})

df_salas_clean = df_salas_clean.rename(
    columns={'Cod_Loc': 'cod_localidad', 'IdProvincia': 'id_provincia', 'IdDepartamento': 'id_departamento',
             'Categoría': 'categoría',
             'Provincia': 'provincia', 'Localidad': 'localidad', 'Nombre': 'nombre', 'Dirección': 'domicilio',
             'CP': 'código postal', 'Teléfono': 'número de teléfono',
             'Mail': 'mail', 'Web': 'web'})

df_bibliotecas_clean = df_bibliotecas_clean.rename(
    columns={'Cod_Loc': 'cod_localidad', 'IdProvincia': 'id_provincia', 'IdDepartamento': 'id_departamento',
             'Categoría': 'categoría',
             'Provincia': 'provincia', 'Localidad': 'localidad', 'Nombre': 'nombre', 'Domicilio': 'domicilio',
             'CP': 'código postal', 'Teléfono': 'número de teléfono',
             'Mail': 'mail', 'Web': 'web'})

df_unificada = pd.concat([df_museos_clean, df_salas_clean, df_bibliotecas_clean], ignore_index=True, sort=False)

"""Registros por fuente, categoría y provincia"""

df_museos2 = df_museos.rename(
    columns={'Fuente': 'fuente', 'Categoría': 'categoria', 'Provincia': 'provincia', 'Nombre': 'nombre'})[
    ['fuente', 'categoria', 'provincia', 'nombre']]

df_salas2 = df_salas.rename(
    columns={'Fuente': 'fuente', 'Categoría': 'categoria', 'Provincia': 'provincia', 'Nombre': 'nombre'})[
    ['fuente', 'categoria', 'provincia', 'nombre']]

df_bibliotecas2 = df_bibliotecas.rename(
    columns={'Fuente': 'fuente', 'Categoría': 'categoria', 'Provincia': 'provincia', 'Nombre': 'nombre'})[
    ['fuente', 'categoria', 'provincia', 'nombre']]

df1 = pd.concat([df_museos2, df_salas2, df_bibliotecas2], ignore_index=True, sort=False)

df_prov = df1.pivot_table(values='nombre', index=['fuente', 'categoria'], columns=['provincia'], aggfunc='count',
                           fill_value=0, margins=True, margins_name='Total')

"""Pantallas, butacas y espacios INCAA por provincia"""

incaa = df_salas[['Provincia', 'Pantallas', 'Butacas', 'espacio_INCAA']]
incaa2 = incaa['espacio_INCAA'].replace('0', np.nan)
incaa['espacio_INCAA'] = incaa2
df_incaa = incaa.groupby(['Provincia']).agg({'Pantallas': 'sum', 'Butacas': 'sum', 'espacio_INCAA': 'count'})