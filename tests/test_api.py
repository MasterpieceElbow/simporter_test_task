import json

import pytest

from app.models import Event


def test_info(client):
    response = client.get("/api/info/")
    assert response.status_code == 200
    assert set(("description", "filtering")) == set(json.loads(response.data).keys())


def test_create_event(client, app):
    response = client.post(
        "/api/create_event/", 
        json={
            "id": "R11QPQWAH45REP",
            "brand": "Downy",
            "asin": "B0014D3N0Q",
            "source": "amazon",
            "stars": 5,
            "timestamp": 1548799200,
        }
    )
    assert response.status_code == 201
    with app.app_context():
        assert Event.query.count() == 1
        assert Event.query.first().id == "R11QPQWAH45REP"


@pytest.mark.parametrize(
    "query,expected",
    [
        ("Grouping=weekly", 
         {'timeline': [
            {'date': '2018-11-01','value': 0},
            {'date': '2018-11-08','value': 0},
            {'date': '2018-11-15','value': 1},
            {'date': '2018-11-22','value': 1},
            {'date': '2018-11-29','value': 0},
            {'date': '2018-12-06','value': 0},
            {'date': '2018-12-13','value': 0},
            {'date': '2018-12-20','value': 1},
            {'date': '2018-12-27','value': 0}]}
        ),
        ("Grouping=bi-weekly", 
         {'timeline': [
            {'date': '2018-11-01','value': 0},
            {'date': '2018-11-15','value': 2},
            {'date': '2018-11-29','value': 0},
            {'date': '2018-12-13','value': 1},
            {'date': '2018-12-27','value': 0}]}
        ),
        ("Grouping=monthly", 
         {'timeline': [
            {'date': '2018-11-01','value': 2},
            {'date': '2018-12-01','value': 1},
            {'date': '2018-12-31','value': 0}]}
        ),
        ("Grouping=weekly&Type=cumulative", 
         {'timeline': [
            {'date': '2018-11-01','value': 0},
            {'date': '2018-11-08','value': 0},
            {'date': '2018-11-15','value': 1},
            {'date': '2018-11-22','value': 2},
            {'date': '2018-11-29','value': 2},
            {'date': '2018-12-06','value': 2},
            {'date': '2018-12-13','value': 2},
            {'date': '2018-12-20','value': 3},
            {'date': '2018-12-27','value': 3}]}
        ),
        ("Grouping=bi-weekly&Type=cumulative", 
         {'timeline': [
            {'date': '2018-11-01','value': 0},
            {'date': '2018-11-15','value': 2},
            {'date': '2018-11-29','value': 2},
            {'date': '2018-12-13','value': 3},
            {'date': '2018-12-27','value': 3}]}
        ),
        ("Grouping=monthly&Type=cumulative", 
         {'timeline': [
            {'date': '2018-11-01','value': 2},
            {'date': '2018-12-01','value': 3},
            {'date': '2018-12-31','value': 3}]}
        ),

    ]
)
def test_timeline_grouping(query, expected, client, events_data):
    response = client.get(f"/api/timeline/?startDate=2018-11-01&endDate=2019-01-01&{query}")
    assert response.status_code == 200
    assert json.loads(response.data) == expected