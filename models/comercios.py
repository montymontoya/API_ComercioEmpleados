from sqlalchemy.schema import Table, Column
from sqlalchemy import types

from sqlalchemy.sql.sqltypes import BigInteger, Boolean, DateTime, BINARY, String
from sqlalchemy.orm import relationship
from config.db import meta, engine

import uuid

comercio = Table("main_comercio",meta,
Column("id",BigInteger, primary_key=True),
Column("uuid",String(), ),
Column("nombre",String(100), ),
Column("activo",Boolean, ),
Column("email_contacto",String(100) ),
Column("telefono_contacto",String(15), ),
Column("api_key",String(), ),
Column("fecha_creacion",DateTime, ),
)

meta.create_all(engine)