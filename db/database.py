from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'sqlite:///instagram.db',
    connect_args={
        'check_same_thread': False,
    },
)
base = declarative_base()

sessionlocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db():
    session = sessionlocal()
    try:
        yield session
    finally:
        session.close()


def create_all_models(base):
    base.metadata.create_all(engine)
