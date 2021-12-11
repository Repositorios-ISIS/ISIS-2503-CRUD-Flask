from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_utils import database_exists, create_database
from local_settings import postgresql as settings
from sqlalchemy.sql import text


def get_engine(user, passwd, host, port, db):
    url = f"postgresql://{user}:{passwd}@{host}:{port}/{db}"
    if not database_exists(url):
        create_database(url)
    engine=create_engine(url, pool_size=50, echo=False)
    return engine

def get_engine_from_settings():
    keys = ['pguser','pgpasswd','pghost','pgport','pgdb']
    if not all(key in keys for key in settings.keys()):
        raise Exception('Bad config file')
    return get_engine(settings['pguser'],
                        settings['pgpasswd'], 
                        settings['pghost'], 
                        settings['pgport'],
                        settings['pgdb'])

def get_session():
    engine = get_engine_from_settings()
    session = scoped_session(sessionmaker(bind=engine))
    return session

"""
engine = get_engine_from_settings()

data = {"nombre":'a',"clave":'123',"cuenta":'123',"direccion":'cra 4'}
statement = text("INSERT INTO restaurante_restaurante(nombre, clave, cuenta, direccion) VALUES (:nombre, :clave, :cuenta, :direccion)")
engine.execute(statement,**data)
"""