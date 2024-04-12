from pytest import fixture
from starlette.testclient import TestClient
from wplt.main import app


@fixture(name="client", scope="session")
def init_app_client():
    return TestClient(app)
