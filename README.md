# API_ComercioEmpleados
Prueba técnica para Bitrend

Este proyecto está basado en el encontrado en https://github.com/alfaro28/comerciosempleados.git

El objetivo de este proyecto es recrear el api, creada en Django, del proyecto original, utilizando FastApi como framework de desarrollo y SQLAlchemy como ORM.

Este proyecto cuenta con la misma base en SQLite del proyecto original más elementos de prueba de api.


## Instalación
Requerimientos:
- Entorno virtual (venv)
- Python 3.9.5, pip

### Entorno de Desarrollo

Para este proyecto se recomienda el uso de un entorno virtual donde se resguardan todas las paqueterías necesarias para la ejecución o edición, así como una instancia de python, sin afectar el software principal.

### Set Up
1. Crear entorno virtual (_venv_)
```shell script 
virtualenv venv
```
2. Activar entorno virtual
```shell script
 ./venv/bin/activate
```
3. Instalar paqueterías de FastAPI y SQLAlchemy. 
```shell script
(venv) pip install -r requirements.txt

```
## Ejecución de servicio
Este proyecto corre bajo _uvicorn_ como servidor y se conecta a una base de datos en SQLite almacenada en la raíz.

Hasta este punto el usuario puede acceder a la información de _comercios_ y _empleados_ contenida en la base de datos mediante el api y get request.

### Arranque de servidor
Para iniciar el servicio, estando el entorno virtual activo y en la raíz del proyecto.
```shell script 
uvicorn app:app
```
Luego de ejecutar esta instrucción deberá poder abrir la ruta http://localhost:8000/ misma que devolverá un texto en pantalla.

### Acceso a datos
Por ahora se puede acceder a toda la información contenida en dos tablas _mainempleado_ y _maincomercio_

Ya iniciado el servicio, para acceder a los datos de comercios usar la ruta
```shell script 
http://localhost:8000/comercios
```

Ya iniciado el servicio, para acceder a los datos de empleados usar la ruta
```shell script 
http://localhost:8000/empleados
```
## Pasos concluídos
0. Estudio y pruebas de proyecto original con Postman y test.py
1. Arranque de proyecto en FastAPI
2. Integración de SQLAlchemy en FastAPI
3. Conexión a base SQLite3 con SQLAlchemy
4. Generación de modelos para las tablas de comercios y empleados en FastAPI
5. Codificación de métodos get simples para obtención de datos de comercio y empleados
## Siguientes pasos
1. Replicar métodos CRUD de Django 
2. Integrar la autenticación por APIKey
3. Integrar excepciones
4. Integrar scripts de test

## Software
FastAPI: (https://fastapi.tiangolo.com/) 
SQLAlchemy: (https://www.sqlalchemy.org/)
Uvicorn: (https://www.uvicorn.org/)