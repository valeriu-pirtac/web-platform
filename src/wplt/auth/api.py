from fastapi.routing import APIRouter

from wplt.config import API_PREFIX

router = APIRouter(prefix=f"{API_PREFIX}/auth", tags=["AUTH"])
