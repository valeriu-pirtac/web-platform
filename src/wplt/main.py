from fastapi import FastAPI

from wplt.auth.api import router as auth_router
from wplt.users.api import router as users_router

app = FastAPI(title="SAP", description="Skills Assessment Platform")

app.include_router(auth_router)
app.include_router(users_router)
