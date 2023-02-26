import pytest

from app import create_app, db
from app.models import Event


@pytest.fixture()
def app():
    app = create_app("sqlite://")

    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def events_data(app):
    for (asin, brand, id_, source, stars, timestamp) in [
        ("B0014D3N0Q", "Downy", "R11QPQWAH45REP", "amazon", 5, 1548799200),
        ("B0014D3N0Q", "Downy", "R3RFSN6FNTQ4JI", "amazon", 5, 1546898400),
        ("B0014D3N0Q", "Downy", "RVEQH20A3EP0A", "amazon", 3, 1546812000),
        ("B0014D3N0Q", "Downy", "RC0ONQQQXLWR9", "amazon", 1, 1545516000),
        ("B0014D3N0Q", "Downy", "R2OHUO09CNTE09", "amazon", 5, 1543269600),
        ("B0014D3N0Q", "Downy", "R1DY51KRE1MFEY", "amazon", 5, 1542751200),
        ("B003IABAS0", "Snuggle", "R1CYYATHTBOMR7", "amazon", 5, 1593723600),
        ("B003IABAS0", "Snuggle", "R3AKTONVR8W63N", "amazon", 5, 1593550800),
        ("B003IABAS0", "Snuggle", "RJYYTXKOTNTTZ", "amazon", 2, 1592686800),
        ("B003IABAS0", "Snuggle", "REO9LW9FYUFFD", "amazon", 5, 1592341200),
        ("B003IABAS0", "Snuggle", "R2ZP7HHA2HFFB4", "amazon", 5, 1591390800),
        ("B003IABAS0", "Snuggle", "R39D7STS9MS3DG", "amazon", 5, 1591045200),
    ]:
        with app.app_context():
            event = Event(
                id=id_,
                asin=asin,
                brand=brand,
                source=source,
                stars=stars,
                timestamp=timestamp,
            )
            db.session.add(event)
            db.session.commit()
