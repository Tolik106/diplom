import sqlalchemy as sq

from sqlalchemy.orm import declarative_base, sessionmaker
from create_tables import create_tables
from create_db import create_db

create_db()

Base = declarative_base()

DSN = 'postgresql://postgres:McDonalds106@localhost:5432/vkinder_db'

engine = sq.create_engine(DSN)



create_tables(engine)




Session = sessionmaker(bind = engine)

session = Session()






session.close()