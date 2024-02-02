from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse

from api.models.parameters import PathParam, QuoteQuery
from api.controllers.requests import fetch_quote

router = APIRouter()


@router.get("/")
async def quotes_root() -> JSONResponse:
    resp = {"status" : "Quotes route running!"}
    return JSONResponse(content=resp, status_code=status.HTTP_200_OK, media_type="application/json")


@router.get("/history-price/dates/{symbol}")
async def history_price(path: PathParam = Depends(), query: QuoteQuery = Depends()) -> JSONResponse:
    query.event = "history"
    resp = fetch_quote(path, query, "URL_QUOTES")
    return JSONResponse(status_code=status.HTTP_200_OK, content=resp, media_type="application/json")


@router.get("/dividend/dates/{symbol}")
async def dividend(path: PathParam = Depends(), query: QuoteQuery = Depends()) -> JSONResponse:
    query.event = "div"
    resp = fetch_quote(path, query, "URL_QUOTES")
    return JSONResponse(status_code=status.HTTP_200_OK, content=resp, media_type="application/json")


@router.get("/stock-split/dates/{symbol}")
async def stock_split(path: PathParam = Depends(), query: QuoteQuery = Depends()) -> JSONResponse:
    query.event = "div"
    resp = fetch_quote(path, query, "URL_QUOTES")
    return JSONResponse(status_code=status.HTTP_200_OK, content=resp, media_type="application/json")
