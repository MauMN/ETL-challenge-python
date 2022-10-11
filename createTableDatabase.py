"""Creación de las tablas en base de datos postgresql (tablas creadas sin datos)"""
from sqlalchemy import create_engine
from sqlalchemy import text
from decouple import config
from pathlib import Path
import logging as log

user = config('USER')
password = config('PASSWORD')
host_name = config('HOST_NAME')
port = config('PORT')
database_name = config('DB_NAME')
create_table_sql = Path(Path.home(), 'create_table.sql')  #adecuar el path hacia el entorno según sea necesario

try:
    database_url = 'postgresql://{}:{}@{}:{}/{}'.format(user, password, host_name, port, database_name)
    # adecuar los datos de conexión para la ejecución en otro ambiente en .env
    engine = create_engine(database_url)
except Exception as e:
    log.error('Error en la conexión a base de datos')
    print(e)
    print('\n')

try:
    with engine.connect() as con:
        with open(create_table_sql) as file:
            query = text(file.read())
            con.execute(query)
except Exception as e:
    log.error ('Error en la ejecución de query create table')
    print(e)
finally:
    con.close()