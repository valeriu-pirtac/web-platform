from fastapi import FastAPI

from wplt.auth.application import endpoints
from wplt.routing import auth, users

app = FastAPI()
app.include_router(auth)
app.include_router(users)
