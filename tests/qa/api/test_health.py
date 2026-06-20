"""Staging API QA — health and platform checks."""
import os

import httpx
import pytest

BASE = os.environ.get("STAGING_API_URL", "https://api-staging.socvault.io/api/v1")
TIMEOUT = 30.0


@pytest.fixture
def client():
    with httpx.Client(base_url=BASE, timeout=TIMEOUT) as c:
        yield c


def test_health_returns_ok(client):
    """T-PLAT-001 — GET /health returns 200 with status field."""
    r = client.get("/health")
    assert r.status_code == 200, r.text
    data = r.json()
    assert data.get("status") in ("ok", "healthy")


def test_openapi_reachable_if_exposed(client):
    """Optional — some deployments expose OpenAPI at /openapi.json."""
    r = client.get("/openapi.json")
    if r.status_code == 404:
        pytest.skip("OpenAPI not exposed on staging API")
    assert r.status_code == 200
