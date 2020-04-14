import pytest

from src.roman.converts import convert_str_to_integer, check_minus_input, check_zero_input,check_int_input


def test_convert_str_to_integer():
    """check_integer() should raise an exception with wrong type param."""
    with pytest.raises(ValueError):
        convert_str_to_integer(input_num="Input a string")


def test_check_minus_raises():
    """check_minus_input() should raise an exception with minus input"""
    with pytest.raises(ValueError) as excinfo:
        check_minus_input(-1)
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Input number is minus. Please input an positive integer!"


def test_check_zero_raises():
    """check_zero_input() should raise an exception with zero input"""
    with pytest.raises(ValueError):
        check_zero_input(0)

def test_check_int_input():
    """check_int_input() should raise an exception with integer input"""
    with pytest.raises(ValueError):
        check_int_input("9")