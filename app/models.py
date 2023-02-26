from .extensions import db


class Event(db.Model):
    __tablename__ = "events"
    id = db.Column(db.String, primary_key=True)
    asin = db.Column(db.String, nullable=False)
    brand = db.Column(db.String, nullable=False)
    source = db.Column(db.String, nullable=False)
    stars = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Event {id}"

    def as_dict(self):
        return {col.name: getattr(self, col.name)
                for col in self.__table__.columns}