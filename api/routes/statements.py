from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse

from api.models.parameters import PathParam, StatementQuery
from api.controllers.requests import fetch_statement

router = APIRouter()


@router.get("/")
async def statements_root() -> JSONResponse:
    resp = {"status" : "Statements route running!"}
    return JSONResponse(content=resp, status_code=status.HTTP_200_OK, media_type="application/json")


@router.get("/income/{symbol}")
async def income(path: PathParam = Depends(), query: StatementQuery = Depends()) -> JSONResponse:
    resp = fetch_statement(path, query, "URL_INCOME_STATEMENT")
    return JSONResponse(content=resp, status_code=status.HTTP_200_OK, media_type="application/json")


@router.get("/balance/{symbol}")
async def balance(path: PathParam = Depends(), query: StatementQuery = Depends()) -> JSONResponse:
    resp = fetch_statement(path, query, "URL_BALANCE_STATEMENT")
    return JSONResponse(content=resp, status_code=status.HTTP_200_OK, media_type="application/json")


@router.get("/cash/{symbol}")
async def cash(path: PathParam = Depends(), query: StatementQuery = Depends()) -> JSONResponse:
    resp = fetch_statement(path, query, "URL_CASH_STATEMENT")
    return JSONResponse(content=resp, status_code=status.HTTP_200_OK, media_type="application/json")
