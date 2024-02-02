from pydantic import BaseModel, Field
from api.models.symbolic_type import Frequency, YearRange, IntervalDate, EventShow
from typing import Optional


class PathParam(BaseModel):
    """Base structure model for the route path parameter."""
    symbol: str = Field(..., max_length=9)


class StatementQuery(BaseModel):
    """Specifically for statements route query parameters."""
    freq: Optional[Frequency] = Frequency.annually


class QuoteQuery(BaseModel):
    """Specifically for quotes route query parameters."""
    range: YearRange = YearRange.one_year
    interval: IntervalDate = IntervalDate.daily
    event: Optional[EventShow] = None
