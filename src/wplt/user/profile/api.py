from fastapi import APIRouter

router = APIRouter(prefix="/profile", tags=["PROFILE"])


@router.get("")
def get_user_profile():
    return "get_user_profile"
