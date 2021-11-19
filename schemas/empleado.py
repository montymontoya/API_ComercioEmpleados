from typing import Optional
from pydantic import BaseModel
from uuid import UUID

class Empleado(BaseModel):
    id: Optional[int]
    uuid: UUID
    nombre: str
    apellidos: str
    pin: str