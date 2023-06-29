import datetime
import json
from decimal import Decimal
import logging
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from scrapy.utils.project import get_project_settings
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
log = logging.getLogger('models')


def _default(val):
    if isinstance(val, Decimal):
        return str(val)
    elif isinstance(val, datetime.datetime):
        return val.isoformat()
    raise TypeError()


def dumps(d):
    return json.dumps(d, default=_default)


def db_connect(**kwargs):
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    settings = get_project_settings()
    kwargs['connect_args'] = {
        "application_name": settings.get('BOT_NAME'),
        'options': '-c lock_timeout=1000 -c statement_timeout=20000'
    }
    return create_engine(settings.get("DATABASE_URL"), json_serializer=dumps, **kwargs)


def create_tables(engine):
    #Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def get_sessionmaker():
    engine = db_connect()
    create_tables(engine)
    return sessionmaker(bind=engine)


Session = get_sessionmaker()


@contextmanager
def get_session(*args, **kwargs):
    session = None
    try:
        session = Session()
        yield session
        session.commit()
    except:
        if session:
            session.rollback()
        raise
    finally:
        if session:
            session.close()
