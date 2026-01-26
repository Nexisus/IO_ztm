import pytest
from calc import add   # albo: from app.calc import add

def test_add_ok():
    assert add(2, 3) == 5

# def test_add_fail_example():
#     assert add(2, 3) == 6


