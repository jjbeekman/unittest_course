from models import Base, Shop
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import pytest


@pytest.fixture
def db_session():
    # Setup
    print("Creating engine")
    engine = create_engine("sqlite:///test.db")
    connection = engine.connect()
    print("Creating tables")
    Base.metadata.bind = connection
    Base.metadata.create_all(engine)
    print("Starting ORM session")
    scoped_db_session = scoped_session(sessionmaker())
    scoped_db_session.configure(bind=connection)
    db_session = scoped_db_session()
    yield db_session

    # Teardown
    print()
    print("Removing scoped db session")
    scoped_db_session.remove()
    print("Dropping tables")
    Base.metadata.drop_all()
    print("Closing connection")
    connection.close()


@pytest.mark.parametrize("run", (1, 2, 3))
def test_db_session(db_session, run):
    # Given
    shop = Shop(name="Test shop")

    # Where
    db_session.add(shop)
    db_session.commit()

    # Then
    shops = db_session.query(Shop).all()
    assert len(shops) == 1
