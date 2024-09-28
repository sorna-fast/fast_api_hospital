from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("mysql://root:26182618m@localhost/hospital_db")

base=declarative_base()



sessionlocal=sessionmaker(bind=engine,autoflush=False)

def get_db():
    global sessionlocal
    session=sessionlocal()
    try:
        yield session
    finally:
        session.close()