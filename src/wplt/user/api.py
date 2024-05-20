from fastapi.routing import APIRouter

from wplt.user.profile.api import router as profile_router

router = APIRouter(prefix="/user", tags=["USER"])

router.include_router(profile_router)


@router.get("")
def get_user():
    return "get_user"
