Backend:
*CREA EL ENTORNO VIRTUAL*
paquete python:
/crea carpeta "venv" y entra a la carpeta/
mkdir venv
cd venv
/instala los paquetes de python y activalos/
python -m venv venv
.\venv\Scripts\Activate.ps1
/para desactivarlo/
source venv\bin\Activate
*INSTALAR LOS PAQUETES*
/flask/
pip install Flask Flask-SQLAlchemy pymysql flask-cors
pip list
/pip install Flask-SQLAlchemy
pip install pymysql
pip install Flask/
