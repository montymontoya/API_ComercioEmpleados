from sqlalchemy import create_engine, text
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.sql.expression import select


engine = create_engine('sqlite:///../db.sqlite3',connect_args={'check_same_thread': False})

conn = engine.connect()
meta = MetaData()