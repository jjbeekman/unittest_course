from models import Shop
import pytest


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
