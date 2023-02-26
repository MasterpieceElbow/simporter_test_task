from flask import Blueprint
from flask_pydantic import validate

from . import schemas, crud
from .extensions import db


api = Blueprint("api", __name__)


@api.route("/info/")
@validate()
def get_info():
    return {
        "description": (
            "'filtering' contains information about "
            "possible filtering and grouping,"
            "where key is an fitler name and string "
            "value means type of filter "
            "and list value means possible choices"
        ),
        "filtering": {
            "startDate": "Date",
            "endDate": "Date",
            "Type": ["usual", "cumulative"],
            "Grouping": ["weekly", "bi-weekly", "monthly"],
            "brand": "String",
            "source": "String",
            "stars": "Integer",
        },
    }


@api.route("/create_event/", methods=["POST"])
@validate()
def create_event(body: schemas.EventCreate):
    crud.create_event(db=db, event=body)
    return {"status": "created"}, 201


@api.route("/events/", methods=["GET"])
@validate()
def get_events():
    events = crud.get_events(db=db)
    return [event.as_dict() for event in events]


@api.route("/timeline/", methods=["GET"])
@validate()
def get_timeline(query: schemas.Timeline):
    timeline = crud.get_timeline(db=db, query=query)
    return {"timeline": timeline}
