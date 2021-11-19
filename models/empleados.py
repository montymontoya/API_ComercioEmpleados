from uuid import UUID
import uuid
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, BigInteger, Boolean, DateTime
from config.db import meta, engine
from models.comercios import comercio

empleado = Table("main_empleado",meta,
Column("id",BigInteger, primary_key=True),
Column("uuid",String(16)),
Column("nombre",String(40), ),
Column("apellidos",String(40), ),
Column("pin",String(6), ),
Column("activo",Boolean, ),
Column("comercio",ForeignKey('main_comercio.id',ondelete="CASCADE")),
Column("fecha_creacion",DateTime, ),
)

meta.create_all(engine)