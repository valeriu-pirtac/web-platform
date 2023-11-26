from fastapi import Body, Query, Response, status
from fastapi.responses import JSONResponse
from pydantic import UUID5

from wplt.auth.domain.models import BaseUser, UserData
from wplt.routing import auth


@auth.get("/login")
async def get_login() -> Response:
    return JSONResponse(content={"page": "Login Page"}, status_code=status.HTTP_200_OK)


@auth.post("/login")
async def post_login(user: BaseUser = Body()) -> Response:
    return JSONResponse(content=user.model_dump(), status_code=status.HTTP_200_OK)


@auth.post("/logout")
async def post_logout(session_id: UUID5 = Query()):
    return {"sesion_id": session_id, "redirect": "/auth/login"}


@auth.get("/register")
async def get_register() -> Response:
    return JSONResponse(
        content={"page": "Register Page"}, status_code=status.HTTP_200_OK
    )


@auth.post("/register")
async def post_register(details: UserData = Body()) -> Response:
    return JSONResponse(
        content=details.model_dump(), status_code=status.HTTP_201_CREATED
    )
