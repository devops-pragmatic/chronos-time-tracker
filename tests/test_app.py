import pytest
from app.app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_health(client):
    """Test the /health endpoint returns 200 and status ok."""
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"
