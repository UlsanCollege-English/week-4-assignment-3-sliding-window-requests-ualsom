import pytest
from src.limiter import RateLimiter

def test_basic_rate_limiting():
    r = RateLimiter(3, 10)
    assert r.allow(1) == True
    assert r.allow(2) == True
    assert r.allow(3) == True
    assert r.allow(4) == False  # limit reached

def test_expiry_allows_again():
    r = RateLimiter(2, 5)
    assert r.allow(1) == True
    assert r.allow(2) == True
    assert r.allow(7) == True  # (1 and 2) are outside window (2 + 5 = 7)

def test_multiple_expiry():
    r = RateLimiter(2, 4)
    assert r.allow(1) == True
    assert r.allow(2) == True
    assert r.allow(3) == False
    assert r.allow(6) == True  # (1, 2) expired, (6) allowed
    assert r.allow(7) == True
    assert r.allow(8) == False
