import pytest
# Test function int_to_roman
from src.roman.converts import int_to_roman, roman_to_int


def test_input_one_output_I():
    assert int_to_roman(1) == "I"


def test_input_five_output_V():
    assert int_to_roman(5) == "V"


def test_input_15_output_XV():
    assert int_to_roman(15) == "XV"


def test_input_42_output_XLII():
    assert int_to_roman(42) == "XLII"


def test_input_9_output_IX():
    assert int_to_roman(9) == "IX"


def test_input_94_output_XCIV():
    assert int_to_roman(94) == "XCIV"


def test_input_1776_output_MDCCLXXVI():
    assert int_to_roman(1776) == "MDCCLXXVI"


# Test function roman_to_int
def test_input_I_output_one():
    assert roman_to_int("I") == 1


def test_input_V_output_five():
    assert roman_to_int("V") == 5


def test_input_XV_output_15():
    assert roman_to_int("XV") == 15


def test_input_XLII_output_42():
    assert roman_to_int("XLII") == 42


def test_input_IX_output_9():
    assert roman_to_int("IX") == 9


def test_input_XCIV_output_94():
    assert roman_to_int("XCIV") == 94


def test_input_MDCCLXXVI_output_1776():
    assert roman_to_int("MDCCLXXVI") == 1776

@pytest.mark.parametrize("test_input, expected", [(1,"I"), (5,"V"), (15,"XV"),(42,"XLII"), (9,"IX"), (94,"XCIV"),(1776,"MDCCLXXVI")])
def test_int_to_roman(test_input, expected):
    assert int_to_roman(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [("I",1), ("V",5), ("XV",15),("XLII",42), ("IX",9), ("XCIV",94),("MDCCLXXVI",1776)])
def test_roman_to_int(test_input, expected):
    assert roman_to_int(test_input) == expected