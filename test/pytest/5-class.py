import pytest
from stuff.accum import accumulator

#--------------------------------------
# TEST
#--------------------------------------
def test_accumulator_init():
    accum = accumulator()
    assert accum.count == 0

def test_accumulator_one():
    accum = accumulator()
    accum.add()
    assert accum.count == 1

def test_accumulator_three():
    accum = accumulator()
    accum.add(3)
    assert accum.count == 3

def test_accumulator_twice():
    accum = accumulator()
    accum.add()
    accum.add()
    assert accum.count == 2

def test_accumulator_directly():
    accum = accumulator()
    with pytest.raises(AttributeError, match=r"can't set attribute") as e:
     accum.count = 10