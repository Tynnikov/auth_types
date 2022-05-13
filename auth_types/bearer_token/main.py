import secrets

from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import (
    HTTPAuthorizationCredentials,
    HTTPBearer,
)
from starlette import status
from starlette.responses import RedirectResponse
from uvicorn import Config, Server

app = FastAPI()

security = HTTPBearer()


def get_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if not secrets.compare_digest(credentials.credentials, "0QGhhHa5iSLGYXH9J1qmy2J-tLsvUyUHoLkf-UGrNo4"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return credentials.credentials


@app.get("/v1/hello")
async def hello_world(_: str = Depends(get_token)):
    return "Hello, World!"


@app.get("/", include_in_schema=False)
async def index() -> RedirectResponse:
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    server = Server(Config("main:app", host="0.0.0.0", port=8000))
    server.run()
