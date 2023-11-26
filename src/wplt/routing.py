from fastapi.routing import APIRouter

auth = APIRouter(prefix="/auth", tags=["authentication"])
users = APIRouter(prefix="/users", tags=["users"])
