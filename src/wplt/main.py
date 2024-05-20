from fastapi import FastAPI

from wplt.auth.api import router as auth_router
from wplt.user.api import router as user_router

app = FastAPI(title="SAP", description="Skills Assessment Platform")

app.include_router(auth_router)
app.include_router(user_router)
