from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, BigInteger, Boolean, DateTime
from config.db import meta, engine

import uuid

from models.comercios import comercio

empleado = Table("main_empleado",meta,
Column("id",BigInteger, primary_key=True),
Column("uuid",String(), ),
Column("nombre",String(40), ),
Column("apellidos",String(40), ),
Column("pin",String(6), ),
Column("activo",Boolean, ),
Column("comercio_id",ForeignKey('comercio.id', related_name='empleados',ondelete="CASCADE")),
Column("fecha_creacion",DateTime, ),
)
