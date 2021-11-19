from fastapi import APIRouter
from fastapi.params import Depends
from starlette.responses import RedirectResponse
from config.db import conn
from config.exception_handler import custom_exception_handler
from config.exceptions import InvalidEmpleadoError, DuplicatedPinError, NoEmpleadoError, \
    IncompleteDataError
from models.empleados import comercio as m_comercio
from models.empleados import empleado as m_empleado
from schemas.empleado import Empleado

from fastapi.security import HTTPBasic, HTTPBasicCredentials

api = APIRouter()
security = HTTPBasic()

@api.get('/')
def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    return RedirectResponse('/empleados')

@api.get('/comercios')
def get_comercios(credentials: HTTPBasicCredentials = Depends(security)):
    current_user = credentials.username
    return conn.execute(m_comercio.select()).fetchall()

@api.get('/empleados')
def get_empleados():
    return conn.execute(m_empleado.select()).fetchall()


@api.get('/empleados/{id}')
def get_empleado(id:str):
    empleado = m_empleado.select().where(m_empleado.c.uuid==id)
    return empleado

@api.post('/empleado')
def post_empleado(empleado_post: Empleado,credentials: HTTPBasicCredentials = Depends(security)):
    comercio = credentials.username
    n_empleado={}
    try:
        n_empleado['nombre'] = empleado_post.nombre
        n_empleado['apellidos'] = empleado_post.apellidos
        n_empleado['pin'] = empleado_post.pin
    except KeyError:
        raise IncompleteDataError()
    n_empleado['id'] = conn.execute(m_empleado.id)
    n_empleado['comercio'] = comercio
    result = conn.execute(m_empleado.insert().values(n_empleado))

    return result

@api.put('/')
def put_empleado():
    return "hello Users"

@api.delete('/empleados')
def delete_empleado():
    return conn.execute(m_empleado.select()).fetchall()
