# Pasos previos para ejecutar el proyecto
* Crearse una base de datos en PostgresSQL de forma local.
* Crear su entorno virtual e instalar las dependencias. 

# Ejecución del proyecto
1. Cambiar el `.env.template` por `.env` y colocar sus credenciales de la db.
2. Crear las migramaciones con el comando `python manage.py makemigrations`.
3. Migrar las tablas a la base de datos con el comando `python manage.py migration`.
4. Ejecutar el comando `python manage.py runserver`.

El proyecto se podrá ver en `http://127.0.0.1:8000/tasks/`