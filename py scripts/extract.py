"""Extracción de datos desde la fuente"""
import os
import logging as log
import requests
import datetime
from requests.exceptions import ConnectionError
from pathlib import Path

año = datetime.datetime.now().strftime("%Y")
mes = datetime.datetime.now().strftime("%B")
mes1 = datetime.datetime.now().strftime("%m")
dia = datetime.datetime.now().strftime("%d")

home = Path(home)  # cambiar la variable "home" de ser necesario
directory_m = 'museos/{}-{}'.format(año, mes)
museos_path = os.path.join(home, directory_m)
directory_s = 'salas/{}-{}'.format(año, mes)
salas_path = os.path.join(home, directory_s)
directory_b = 'bibliotecas/{}-{}'.format(año, mes)
biblios_path = os.path.join(home, directory_b)

if __name__ == '__main__':
    log.basicConfig(level=log.INFO)
    try:
        museos = requests.get(
            "https://docs.google.com/spreadsheets/d/1PS2_yAvNVEuSY0gI8Nky73TQMcx_G1i18lm--jOGfAA/export?format=csv&id"
            +"=1PS2_yAvNVEuSY0gI8Nky73TQMcx_G1i18lm--jOGfAA&gid=514147473",
            allow_redirects=True)
        os.makedirs(museos_path, exist_ok=True)  #las carpetas y los archivos se crearán desde el directorio home
        open('{}/museos-{}-{}-{}.csv'.format(museos_path, dia, mes1, año), 'wb').write(museos.content)
        log.info('museos cargada correctamente')
    except ConnectionError as e:
        log.error('Error en la request')
        print(e)
        print('\n')

    try:
        salas = requests.get(
            "https://docs.google.com/spreadsheets/d/1o8QeMOKWm4VeZ9VecgnL8BWaOlX5kdCDkXoAph37sQM/export?format=csv&id"
            +"=1o8QeMOKWm4VeZ9VecgnL8BWaOlX5kdCDkXoAph37sQM&gid=1691373423",
            allow_redirects=True)
        os.makedirs(salas_path, exist_ok=True)
        open('{}/salas-{}-{}-{}.csv'.format(salas_path, dia, mes1, año), 'wb').write(salas.content)
        log.info('salas de cine cargada correctamente')
    except ConnectionError as e:
        log.error('Error en la request')
        print(e)
        print('\n')

    try:
        bibliotecas = requests.get(
            'https://docs.google.com/spreadsheets/d/1udwn61l_FZsFsEuU8CMVkvU2SpwPW3Krt1OML3cYMYk/export?format=csv&id'
            +'=1udwn61l_FZsFsEuU8CMVkvU2SpwPW3Krt1OML3cYMYk&gid=1605800889',
            allow_redirects=True)
        os.makedirs(biblios_path, exist_ok=True)
        open('{}/bibliotecas-{}-{}-{}.csv'.format(biblios_path, dia, mes1, año), 'wb').write(bibliotecas.content)
        log.info('bibliotecas cargada correctamente')
    except ConnectionError as e:
        log.error('Error en la request')
        print(e)
        print('\n')
