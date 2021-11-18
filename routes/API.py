from fastapi import APIRouter
import sqlalchemy
from config.db import conn
from models.comercios import comercio
from models.empleados import empleado

api = APIRouter()

@api.get('/empleados')
def get_empleados():
    return conn.execute(empleado.select()).fetchall()

@api.get('/comercios')
def get_comercios():
    return conn.execute(comercio.select()).fetchall()


@api.get('/')
def index():
    return "hello Users"