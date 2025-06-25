import pytest 
def test_div_zero ():    
    with pytest.raises(ZeroDivisionError) as e: #1
        num = 1/0
    assert 'division by zero' in  str(e.value) #2


    
