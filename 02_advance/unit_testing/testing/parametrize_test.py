import pytest

def add(a,b):
    return a + b

# The test function is marked with the "@pytest.mark.parametrize" decorator
@pytest.mark.parametrize("x, y , expected_output", [
    (1, 2, 100), # Failed
    (2, 4, 6),
    (0, 0, 0),
    (-1, -2, -3)
])
def test_multiply_by_two(x, y, expected_output):
    result = add(x,y)
    assert result == expected_output
