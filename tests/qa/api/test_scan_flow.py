"""Staging API QA — L1 scan user stories US-008–US-010."""
import os

import httpx
import pytest

BASE = os.environ.get("STAGING_API_URL", "https://api-staging.socvault.io/api/v1")
TIMEOUT = 120.0
TOKEN = os.environ.get("STAGING_ACCESS_TOKEN", "")


pytestmark = pytest.mark.skipif(
    not os.environ.get("STAGING_ACCESS_TOKEN"),
    reason="Set STAGING_ACCESS_TOKEN for scan tests (from verify-otp on staging)",
)


@pytest.fixture
def auth_client():
    headers = {"Authorization": f"Bearer {TOKEN}"}
    with httpx.Client(base_url=BASE, timeout=TIMEOUT, headers=headers) as c:
        yield c


def test_l1_scan_execute(auth_client):
    """T-004 / US-008 — POST /scan/execute starts L1 scan."""
    r = auth_client.post(
        "/scan/execute",
        json={"layer": "L1", "target": os.environ.get("STAGING_TEST_DOMAIN", "example.com"), "scan_authorised": True},
    )
    if r.status_code == 503:
        pytest.skip("Scan service not deployed on staging yet")
    assert r.status_code in (200, 201, 202), r.text
    data = r.json()
    assert "scan_id" in data or "id" in data


def test_freemium_rate_limit(auth_client):
    """T-003 / US-010 — second scan in same month returns 429."""
    pytest.skip("Run manually after two scans in same calendar month")


def test_tenant_isolation(auth_client):
    """T-008 — tenant A cannot read tenant B scan."""
    pytest.skip("Requires two staging tokens — implement when multi-tenant QA data exists")
