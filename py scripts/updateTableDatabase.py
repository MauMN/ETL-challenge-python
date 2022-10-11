"""Actualización de las tablas en base de datos postgresql a partir de los datos procesados"""
"""Populando las tablas con dichos datos procesados y/o reemplazando los existentes de haberlos"""
import datetime
import logging as log
from sqlalchemy import create_engine
from process import df_unificada, df_prov, df_incaa
from decouple import config

user = config('USER')
password = config('PASSWORD')
host_name = config('HOST_NAME')
port = config('PORT')
database_name = config('DB_NAME')

try:
    database_url = 'postgresql://{}:{}@{}:{}/{}'.format(user, password, host_name, port, database_name)
    # adecuar los datos de conexión para la ejecución en otro ambiente en .env
    engine = create_engine(database_url)
except Exception as e:
    log.error('Error en la conexión a base de datos')
    print(e)
    print('\n')

x = datetime.datetime.now()

df_unificada['Fecha_carga'] = x.strftime("%c")
df_prov['Fecha_carga'] = x.strftime("%c")
df_incaa['Fecha_carga'] = x.strftime("%c")

df_unificada.to_sql('tabla_unificada', con=engine, if_exists='replace')
df_prov.to_sql('provincias_fuentes', con=engine, if_exists='replace')
df_incaa.to_sql('pantallas_butacas_incaa', con=engine, if_exists='replace')