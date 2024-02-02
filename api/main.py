from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from api.routes import statements, quotes

# Create a asynchronouos server gateway interface
app = FastAPI()

# Connnect the routes
app.include_router(statements.router, prefix="/statements")
app.include_router(quotes.router, prefix="/quotes")


@app.get("/")
async def root() -> JSONResponse:
    resp = {"status" : "Server running!"}
    return JSONResponse(content=resp, status_code=status.HTTP_200_OK, media_type="application/json")
