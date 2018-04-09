from contextlib import contextmanager
import os

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.exc import IntegrityError, ProgrammingError
from sqlalchemy.orm import sessionmaker

from models import Base


@contextmanager
def session_scope(
        username=os.environ['PGUSER'],
        password=os.environ['PGPASSWORD'],
        host=os.environ['PGHOST'],
        port=os.environ['PGPORT'],
        database=os.environ['PGDATABASE'],
        echo=False,
        raise_integrity_error=True,
        raise_programming_error=True
):
    """Provide a transactional scope around a series of operations."""
    postgres_url = URL(
        drivername='postgresql+psycopg2',
        username=username,
        password=password,
        host=host,
        port=port,
        database=database
    )

    engine = create_engine(postgres_url,
                           echo=echo,
                           connect_args={'sslmode': 'require'}
                           )
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    try:
        yield session
        session.commit()
    except IntegrityError:
        session.rollback()
        if raise_integrity_error:
            raise
    except ProgrammingError:
        session.rollback()
        if raise_programming_error:
            raise
    except:
        session.rollback()
        raise
    finally:
        session.close()


def create_database(echo=True):
    with session_scope(echo=echo) as session:
        Base.metadata.create_all(session.connection())


def drop_database(echo=True):
    with session_scope(echo=echo) as session:
        Base.metadata.drop_all(session.connection())


if __name__ == '__main__':
    create_database()
