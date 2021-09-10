import pytest

import mathlib


# @pytest.mark.windows
# def test_add_num():
# 	result = mathlib.add_num(2,3)
# 	assert result == 5

@pytest.mark.skip(reason="Dont want multiplication right now")
def test_mul():
    result = mathlib.mul_num(2, 3)
    assert result == 6


@pytest.mark.parametrize("num, result",
                         [
                             (1, 1),
                             (2, 4)
                         ])
def test_square(num, result):
    res = mathlib.square(num)
    assert res == result


# ----------------------------------------------------

@pytest.fixture
def wake_up_cpu(scope="module"):
    up = True
    if up:
        print(" --- CPU is woke up")
        return True
    print("--- CPU is down")
    return up


def test_mul1(wake_up_cpu):
    if wake_up_cpu is True:
        result = mathlib.mul_num(6, 3)
        assert result == 18
    else:
        raise IOError
