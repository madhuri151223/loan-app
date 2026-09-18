
from app import calculate_interest

def test_interest():
    assert calculate_interest(10000, 10) == 1000
