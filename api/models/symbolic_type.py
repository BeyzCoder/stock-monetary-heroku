from enum import Enum


class YearRange(str, Enum):
    """Years choices."""
    one_year = "1y"
    five_year = "5y"
    max_year = "MAX"


class IntervalDate(str, Enum):
    """Interval choices."""
    daily = "1d"
    weekly = "1wk"
    monthly = "1mo"


class EventShow(str, Enum):
    """Event choices."""
    history = "history"
    dividend = "div"
    stock_split = "split"


class Frequency(str, Enum):
    """Data frequency."""
    annually = "annually"
    quarterly = "quarterly"
