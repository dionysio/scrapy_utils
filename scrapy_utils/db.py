import datetime
import uuid
import json
from decimal import Decimal
import logging
from contextlib import contextmanager

from sqlalchemy import create_engine, Column, ForeignKey, UniqueConstraint, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, DateTime, Float, Boolean, Text, JSON, Index, func)
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


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("DATABASE_URL"), json_serializer=dumps)


def create_tables(engine):
    Base.metadata.drop_all(engine)
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
