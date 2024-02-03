from api.models.parameters import PathParam, StatementQuery, QuoteQuery
from pydantic import ValidationError
import pytest


def test_path_param_model() -> None:
    # Success unit test
    path_param = PathParam(symbol="ABCDEFGHI")
    assert path_param.symbol == "ABCDEFGHI"

    # Fail unit test
    with pytest.raises(ValidationError):
        path_param = PathParam(symbol="ABCDEFGHIJ")

    with pytest.raises(ValidationError):
        path_param = PathParam(symbol=123)


def test_statement_param_model() -> None:
    # Success unit test
    statement_query = StatementQuery()
    assert statement_query.freq == "annually"

    statement_query = StatementQuery(freq="annually")
    assert statement_query.freq == "annually"

    statement_query = StatementQuery(freq="quarterly")
    assert statement_query.freq == "quarterly"

    # Fail unit test
    with pytest.raises(ValidationError):
        statement_query = StatementQuery(freq="egg")

    with pytest.raises(ValidationError):
        statement_query = StatementQuery(freq=123)


def test_quote_param_model() -> None:
    # Success unit test
    quote_query = QuoteQuery()
    assert quote_query.range == "1y"
    assert quote_query.interval == "1d"
    assert quote_query.events is None

    quote_query = QuoteQuery(range="5y", interval="1wk", events="history")
    assert quote_query.range == "5y"
    assert quote_query.interval == "1wk"
    assert quote_query.events == "history"

    quote_query = QuoteQuery(range="MAX", interval="1mo", events="div")
    assert quote_query.range == "MAX"
    assert quote_query.interval == "1mo"
    assert quote_query.events == "div"

    with pytest.raises(ValidationError):
        quote_query = QuoteQuery(range="8y", interval="1d", events="split")

    with pytest.raises(ValidationError):
        quote_query = QuoteQuery(range="5y", interval="2d", events="history")

    with pytest.raises(ValidationError):
        quote_query = QuoteQuery(range="MAX", interval="1wk", events="year")
