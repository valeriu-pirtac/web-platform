from fastapi import Depends
from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from wplt.config import API_PREFIX

router = APIRouter(prefix=f"{API_PREFIX}/auth", tags=["AUTH"])


@router.post("/token")
async def login_form(form_data: OAuth2PasswordRequestForm = Depends()):
    return {
        "username": form_data.username,
        "password": form_data.password,
        "role": "guest",
    }
