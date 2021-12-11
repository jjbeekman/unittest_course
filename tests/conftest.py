# Anything that is defined here, will be run during the test discovery phase of pytest
from models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import pytest


@pytest.fixture
def connection():
    # Setup
    print("Creating engine")
    engine = create_engine("sqlite:///test.db")
    connection = engine.connect()
    yield connection

    # Teardown
    print("Closing connection")
    connection.close()


@pytest.fixture
def setup_database(connection):
    # Setup
    print("Creating tables")
    Base.metadata.bind = connection
    Base.metadata.create_all()
    yield

    # Teardown
    print("Dropping tables")
    Base.metadata.drop_all()


@pytest.fixture
def db_session(connection, setup_database):
    # Setup
    print("Starting ORM session")
    scoped_db_session = scoped_session(sessionmaker())
    scoped_db_session.configure(bind=connection)
    db_session = scoped_db_session()
    yield db_session

    # Teardown
    print()
    print("Removing scoped db session")
    scoped_db_session.remove()
