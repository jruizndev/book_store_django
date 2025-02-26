# Comandos Esenciales para Proyectos Django

Este documento es una referencia rápida para gestionar proyectos Django, con especial enfoque en el entorno virtual, la gestión de paquetes y los comandos esenciales de Django.

## Entorno Virtual

```bash
# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows

# Desactivar entorno virtual
deactivate
```

## Gestión de Paquetes

```bash
# Instalar dependencias con uv 
uv pip install django djangorestframework python-dotenv
uv pip install mysqlclient     # Para MySQL
uv pip install psycopg2-binary # Para PostgreSQL

# Guardar dependencias
uv pip freeze > requirements.txt

# Instalar dependencias desde un archivo
uv pip install -r requirements.txt

# Ver paquetes instalados
uv pip list
```

## Comandos Django

```bash
# Crear un nuevo proyecto
django-admin startproject nombre_proyecto .

# Crear una nueva aplicación dentro del proyecto
python manage.py startapp nombre_app

# Ejecutar el servidor de desarrollo
python manage.py runserver
python manage.py runserver 8080
python manage.py runserver 0.0.0.0:8000

# Migraciones
python manage.py makemigrations
python manage.py migrate
python manage.py showmigrations
python manage.py sqlmigrate nombre_app 0001

# Crear un superusuario
python manage.py createsuperuser
python manage.py changepassword usuario

# Acceder a la shell interactiva de Django
python manage.py shell

# Verificar el estado del proyecto
python manage.py check
python manage.py check --deploy

# Limpiar sesiones de la base de datos
python manage.py clearsessions

# Recolectar archivos estáticos
python manage.py collectstatic

# Ejecutar tests
python manage.py test
python manage.py test nombre_app
```

## Comandos MySQL

```bash
# Acceder a MySQL desde la terminal
mysql -u usuario -p

# Crear una base de datos desde MySQL
CREATE DATABASE nombre_db;

# Listar bases de datos disponibles
SHOW DATABASES;

# Usar una base de datos específica
USE nombre_db;

# Crear una base de datos sin ingresar a MySQL
mysql -u usuario -p -e "CREATE DATABASE nombre_db"
```


