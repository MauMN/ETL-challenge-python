# Alkemy challenge python
Repositorio con resolución del challenge de ingreso alkemy data analytics + python

Para el correcto deploy se deben seguir los siguientes pasos, ejecutando los comandos desde el command prompt:

Instalamos la libreria de entornos virtuales, venv:

pip install virtualenv

Posicionamos el current directory en la dirección donde queremos instalar el entorno virtual (puede ser el home del SO pero no necesariamente), y lo creamos con el comando:

python -m venv nombre_del_entorno

Lo activamos:

[path]\nombre_del_entorno\Scripts\activate

Con el entorno instalado y activado instalamos las librerías necesarias:

pip install pandas<br/>
pip install SQLAlchemy<br/>
pip install psycopg2<br/>
pip install requests<br/>
pip install datetime<br/>
pip install logging<br/>
pip install pathlib<br/>
pip install python-decouple<br/>

Para conectar a base de datos, adecuamos el archivo .env con la configuración de los datos de conexión que constituuyen la database_url (user, pass, admin, host_name,
port, database_name) del administrador local de PostgreSQL.

Finalmente ejecutamos los scripts .py en orden para la extracción, procesamiento y carga a base de datos:

python extract.py<br/>
python process.py<br/>
python createTableDatabase.py<br/>
python updateTableDatabase.py
