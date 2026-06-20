"""Staging API QA — auth user stories US-001–US-007."""
import os
import uuid

import httpx
import pytest

BASE = os.environ.get("STAGING_API_URL", "https://api-staging.socvault.io/api/v1")
TIMEOUT = 30.0


@pytest.fixture
def client():
    with httpx.Client(base_url=BASE, timeout=TIMEOUT) as c:
        yield c


def test_reject_freemail_signup(client):
    """T-001 / US-002 — freemail domains rejected."""
    r = client.post(
        "/auth/signup",
        json={"email": "notallowed@gmail.com", "phone": "+447700900001"},
    )
    assert r.status_code in (400, 422), r.text


def test_signup_accepts_business_email(client):
    """T-002 / US-001 — business email accepted (OTP sent)."""
    domain = os.environ.get("STAGING_TEST_DOMAIN", "example.com")
    uid = uuid.uuid4().hex[:8]
    email = os.environ.get("STAGING_TEST_EMAIL") or f"qa+{uid}@{domain}"
    phone = os.environ.get("STAGING_TEST_PHONE", "+447700900002")
    r = client.post("/auth/signup", json={"email": email, "phone": phone})
    if r.status_code == 503:
        pytest.skip("Auth service not deployed on staging yet")
    assert r.status_code in (200, 201, 202), r.text


def test_me_requires_auth(client):
    """T-007 / US-007 — GET /auth/me without token returns 401."""
    r = client.get("/auth/me")
    assert r.status_code == 401, r.text
