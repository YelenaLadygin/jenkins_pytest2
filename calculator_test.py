import pytest
import calculator

def test_calc_add():
    assert calculator.calc_add(2,4)==6

def test_calc_diff():
    assert calculator.calc_diff(10,5)==5

def test_calc_multp():
    assert calculator.calc_multp(2,4)==8


def test_app_div():
    assert calculator.calc_div(33,11)==3

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
         calculator.calc_div(3, 0)

@pytest.fixture
def five():
    return 5

@pytest.mark.calc
def test_add_operation(five):
   assert calculator.calc_add(five, 7) == 12

@ pytest.mark.parametrize("x", [1, 2, 3, 4, 5])
def test_add_operation_with_parameterize(x):
        assert calculator.calc_add(5, x) == 5 + x

@ pytest.mark.parametrize("x", [1, 2, 3])
def test_add_operation_with_parameterize(x):
        assert calculator.calc_multp(3, x) == 3 * x




