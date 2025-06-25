import pytest
from stuff.accum import accumulator

#--------------------------------------
# Fixtures
#--------------------------------------
@pytest.fixture
def accum():
    return accumulator()
#--------------------------------------
# TEST
#--------------------------------------
def test_accumulator_init(accum):    
    assert accum.count == 0

def test_accumulator_one(accum):    
    accum.add()
    assert accum.count == 1

def test_accumulator_three(accum):    
    accum.add(3)
    assert accum.count == 3

def test_accumulator_twice(accum):    
    accum.add()
    accum.add()
    assert accum.count == 2

def test_accumulator_directly(accum):    
    with pytest.raises(AttributeError, match=r"can't set attribute") as e:
     accum.count = 10