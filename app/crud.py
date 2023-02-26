from datetime import datetime, timedelta

from sqlalchemy import func, select

from . import schemas
from . import models


def create_event(event: schemas.EventCreate, db):
    event = models.Event(**event.dict())
    db.session.add(event)
    db.session.commit()


def get_events(db):
    return db.session.execute(select(models.Event)).scalars().all()


def group_by_days(
    days: int,
    events: list[tuple[str, int]],
    start: datetime.date,
    end: datetime.date,
) -> dict[str, int]:
    group = {}
    date_ = start
    while date_ < end:
        group[date_] = 0
        date_ += timedelta(days)
    for date_, count in events:
        event_date = datetime.strptime(date_, "%Y-%m-%d").date()
        diff = (event_date - start).days % days
        group[event_date - timedelta(diff)] += count
    return {str(date_): count for date_, count in group.items()}


def to_cumulative(group: dict[str, int]) -> None:
    sum = 0
    for key in group:
        group[key] += sum
        sum = group[key]


def get_timeline(db, query: schemas.Timeline) -> list[dict]:
    queryset = select(
        func.date(models.Event.timestamp, "unixepoch"),
        func.count(models.Event.id),
    ).filter(
        func.date(models.Event.timestamp, "unixepoch") < query.endDate,
        func.date(models.Event.timestamp, "unixepoch") >= query.startDate,
    )
    if query.asin:
        queryset = queryset.filter(models.Event.asin == query.asin)
    if query.brand:
        queryset = queryset.filter(models.Event.brand == query.brand)
    if query.source:
        queryset = queryset.filter(models.Event.source == query.source)
    if query.stars:
        queryset = queryset.filter(models.Event.stars == query.stars)

    queryset = queryset.group_by(
        func.date(models.Event.timestamp, "unixepoch")
    ).order_by(models.Event.timestamp)

    events = db.session.execute(queryset).all()
    if query.Grouping == schemas.TimelineGrouping.weekly:
        group = group_by_days(
            days=7, events=events, start=query.startDate, end=query.endDate
        )
    elif query.Grouping == schemas.TimelineGrouping.bi_weekly:
        group = group_by_days(
            days=14, events=events, start=query.startDate, end=query.endDate
        )
    elif query.Grouping == schemas.TimelineGrouping.monthly:
        group = group_by_days(
            days=30, events=events, start=query.startDate, end=query.endDate
        )

    if query.Type == schemas.TimelineType.cumulative:
        to_cumulative(group=group)

    return [{"date": date_, "value": count} for date_, count in group.items()]
