from fastapi import FastAPI

from wplt.auth.api import router as auth_router
from wplt.config import API_V1_STR
from wplt.user.api import router as user_router

app = FastAPI(
    title="SAP",
    description="Skills Assessment Platform",
    root_path=API_V1_STR,
)

app.include_router(auth_router, prefix=API_V1_STR)
app.include_router(user_router, prefix=API_V1_STR)
