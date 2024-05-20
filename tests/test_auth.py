from fastapi import status
from starlette.testclient import TestClient


def test_login_with_username_and_password(client: TestClient):
    credentials = {"username": "admin", "password": "admin"}

    response = client.post(url="/api/v1/auth/token", data=credentials)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["username"] == credentials["username"]
    assert response.json()["password"] == credentials["password"]
    assert response.json()["role"] == "guest"
