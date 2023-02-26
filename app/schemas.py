from pydantic import BaseModel
from datetime import date
from typing import Optional
from enum import Enum


class TimelineType(str, Enum):
    usual = "usual"
    cumulative = "cumulative"


class TimelineGrouping(str, Enum):
    weekly = "weekly"
    bi_weekly = "bi-weekly"
    monthly = "monthly"


class EventCreate(BaseModel):
    id: str
    asin: str
    brand: str
    source: str
    stars: int
    timestamp: int


class Timeline(BaseModel):
    startDate: date
    endDate: date
    Type: Optional[TimelineType] = TimelineType.usual
    Grouping: TimelineGrouping
    asin: Optional[str]
    brand: Optional[str]
    source: Optional[str]
    stars: Optional[int]
