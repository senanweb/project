import pytest

products = [
    (2, 3, 6),                 # postive integers
    (1, 99, 99),               # identity
    (0, 99, 0),                # zero
    (3, -4, -12),              # postive by integers
    (-5, -5, 25),              # integers by integers
    (2.5, 6.7, 16.75)          # floats
]


# to work @pytest.mark.parametrize must import pytest
@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product
