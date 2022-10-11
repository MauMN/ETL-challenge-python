<h1><b>Alkemy challenge python</b></h1>
<h3><i>Repositorio con resolución del Challenge de ingreso Alkemy Data Analytics + Python</i></h3>

Para el correcto deploy se deben seguir los siguientes pasos, ejecutando los comandos desde el command prompt:

Instalamos la libreria de entornos virtuales, virtualenv:

pip install virtualenv

Posicionamos el current directory en la dirección donde queremos instalar el entorno virtual (puede ser el home del SO pero no necesariamente), y lo creamos con el comando:

virtualenv nombre_del_entorno<br/>
o<br/>
python -m venv nombre_del_entorno (para utilizar el paquete venv soportado por python3, pero no por versiones más antiguas)

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

Para conectar a base de datos, adecuamos el archivo .env con la configuración de los datos de conexión que constituyen la database_url (user, pass, admin, host_name,
port, database_name) del administrador local de PostgreSQL.

Finalmente ejecutamos los scripts .py en orden para la extracción, procesamiento y carga a base de datos:

python extract.py<br/>
python process.py<br/>
python createTableDatabase.py<br/>
python updateTableDatabase.py
