import pytest

from src.roman.converts import int_to_roman, roman_to_int


@pytest.mark.parametrize("test_input, expected",
                         [(1, "I"), (5, "V"), (15, "XV"), (42, "XLII"), (9, "IX"), (94, "XCIV"), (1776, "MDCCLXXVI")])
def test_int_to_roman(test_input, expected):
    assert int_to_roman(test_input) == expected


@pytest.mark.parametrize("test_input, expected",
                         [("I", 1), ("V", 5), ("XV", 15), ("XLII", 42), ("IX", 9), ("XCIV", 94), ("MDCCLXXVI", 1776)])
def test_roman_to_int(test_input, expected):
    assert roman_to_int(test_input) == expected


# Parametrizing tests with data
int_to_roman_data = [(1, "I"), (5, "V"), (15, "XV"), (42, "XLII"), (9, "IX"), (94, "XCIV"), (1776, "MDCCLXXVI")]
roman_to_int_data = [("I", 1), ("V", 5), ("XV", 15), ("XLII", 42), ("IX", 9), ("XCIV", 94), ("MDCCLXXVI", 1776)]


@pytest.mark.parametrize("test_input, expected", int_to_roman_data)
def test_int_to_roman_with_data(test_input, expected):
    assert int_to_roman(test_input) == expected


@pytest.mark.parametrize("test_input, expected", roman_to_int_data)
def test_roman_to_int_with_data(test_input, expected):
    assert roman_to_int(test_input) == expected
